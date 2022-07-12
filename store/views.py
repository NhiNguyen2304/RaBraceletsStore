from unicodedata import category
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from sqlalchemy import true
import sqlalchemy
from .models import Category, Bracelet, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db

# This data will eventually be stored in a database
# sydney = City('1', 'Sydney', 'City in New South Wales with largest population', 'sydney.jpg')
# brisbane = City('2', 'Brisbane', 'City in Queensland with a good weather', 'brisbane.jpg')
# tour1 = Tour('1', 'Kangaroo point walk', 'Gentle stroll but be careful of cliffs. Hand feed the kangaroos', 't_hand.jpg', 99.00, brisbane, datetime(2020,7,23))
# tour2 = Tour('2', 'West End markets', 'Tour the boutique goods and food and ride the wheel', 't_ride.jpg', 20.00, brisbane, datetime(2019,10,30))
# tour3 = Tour('3', 'Whale spotting', 'Visit Straddy and see the whales migrating', 't_whale.jpg', 129.00, sydney, datetime(2019,10,30))
# cities = [brisbane,sydney]
# tours = [tour1,tour2,tour3]
# order1 = Order('1', False, '', '','', '', datetime.now(), [tour1,tour2], tour1.price+tour2.price) # simulating order not checked out
# order2 = Order('2', False, '', '','', '', datetime.now(), [tour3], tour1.price+tour3.price) # simulating order not checked out
# orders = [order1,order2]

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    # braceletsChains = Bracelet.query.order_by(Bracelet.name).filter_by(category_id = '1').limit(4)
    # braceletsLeathers = Bracelet.query.order_by(Bracelet.name).filter_by(category_id = '2').limit(4)
    # braceletsStones = Bracelet.query.order_by(Bracelet.name).filter_by(category_id = '3').limit(4)
    
    #categories = Category.query.order_by(Category.name).all()
    #bracelets = db.session.query(Bracelet).from_statement(sqlalchemy.text("SELECT * FROM bracelets b JOIN categories c ON b.category_id = c.id ORDER BY category_id"))
    bracelets = Bracelet.query.order_by(Bracelet.name).limit(12)
    return render_template('index.html', categories = getMenu(), orderCount = getNumberOfOrder(), bracelets = bracelets)
    # q = db.session.query(Bracelet).from_statement(sqlalchemy.text("SELECT * FROM bracelets b JOIN categories c ON b.category_id = c.id WHERE b.id = '1'"))
    # bracelet = q.first()
    # print(bracelet)
    # return render_template('test.html', bracelet = bracelet)


@bp.route('/aboutUs')
def getAboutUs():
    categories = Category.query.order_by(Category.name).all()
    return render_template('aboutUs.html', categories = getMenu(), orderCount = getNumberOfOrder())

@bp.route('/bracelets/<int:categoryid>/')
def getsubcategory(categoryid):
    braceincategory = Bracelet.query.filter(Bracelet.category_id == categoryid)
    category = Category.query.get(categoryid)
    return render_template('sub_category.html', orderCount = getNumberOfOrder(), category = category, braceincategory = braceincategory, categories = getMenu())

@bp.route('/bracelet_detail/<int:categoryid>/<int:braceletid>/')
def getproductdetails(braceletid, categoryid):
    braceletdetails = Bracelet.query.filter(Bracelet.id == braceletid)
    #category = Category.query(Category).join(Bracelet, Bracelet.category_id == Category.id).filter(Bracelet.id == braceletid).one()
    category = Category.query.get(categoryid)
    return render_template('product_detail.html', orderCount = getNumberOfOrder(), category = category, braceletdetails = braceletdetails, categories = getMenu())

@bp.route('/bracelets/')
def search():
    search = request.args.get('search')
    search_content = search
    search = '%{}%'.format(search) # substrings will match
    bracelets = Bracelet.query.filter(Bracelet.name.like(search)).all()
    #category = db.session.query(Bracelet).from_statement(sqlalchemy.text("SELECT category_id FROM bracelets b JOIN categories c ON b.category_id = c.id WHERE b.name LIKE :search", {'search': search}))
    if not bracelets:
        isEmpty = 1
    else:
        isEmpty = 0
    return render_template('search_detail.html', orderCount = getNumberOfOrder(), search_content = search_content, isEmpty = isEmpty, bracelets = bracelets, categories = getMenu())

# Referred to as "Basket" to the user
@bp.route('/order', methods=['POST','GET'])
def order():
    bracelet_id = request.values.get('bracelet_id')

    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(username='', address='', phone='', status=False, totalprice=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    countOrder = 0
    if order is not None:
        for bracelet in order.bracelets:
            countOrder = countOrder + 1
            totalprice = totalprice + bracelet.price
    
    # are we adding an item?
    if bracelet_id is not None and order is not None:
        bracelet = Bracelet.query.get(bracelet_id)
        if bracelet not in order.bracelets:
            try:
                order.bracelets.append(bracelet)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('item already in basket')
            return redirect(url_for('main.order'))
    
    if not order:
        isEmpty = 1
    else:
        isEmpty = 0

    # query = db.session.query(order.bracelets).from_statement(sqlalchemy.text("SELECT count(order_id) FROM orderdetails WHERE order_id = (SELECT MAX(order_id) FROM orderdetails) GROUP BY order_id"))
    # countorder = query.first()
    return render_template('order.html', order = order, orderCount = getNumberOfOrder(), totalprice = totalprice, isEmpty = isEmpty, categories = getMenu())

@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        bracelet_to_delete = Bracelet.query.get(id)
        try:
            order.bracelets.remove(bracelet_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'), categories = getMenu(), orderCount = getNumberOfOrder())

# Scrap basket
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))

# Referred to as "Basket" to the user
@bp.route('/placeorder')
def placeorder():
    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for bracelet in order.bracelets:
            totalprice = totalprice + bracelet.price
    
    return render_template('place_order.html', order = order, totalprice = totalprice, categories = getMenu(), orderCount = getNumberOfOrder())

@bp.route('/checkout', methods=['POST','GET'])
def checkout():
        # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for bracelet in order.bracelets:
            totalprice = totalprice + bracelet.price
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
       
        if form.validate_on_submit():
            order.username = form.username.data
            order.phone = form.phone.data
            order.address = form.address.data
            order.status = True
            totalcost = 0
            for bracelet in order.bracelets:
                totalcost = totalcost + bracelet.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you for your order! We will contact you to confirm!')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('place_order.html', form = form, order = order, totalprice = totalprice, categories = getMenu(), orderCount = getNumberOfOrder())

def getMenu():
    categories = Category.query.order_by(Category.name).all()
    return categories

def getNumberOfOrder():
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None
    
    countOrder = 0
    if order is not None:
        for bracelet in order.bracelets:
            countOrder = countOrder + 1

    return countOrder

