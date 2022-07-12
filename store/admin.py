'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    #from store import db, create_app
    #db.create_all(app=create_app())
    from store import db, create_app
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.create_all()

    from store.models import Category, braceletinsizes, Bracelet, Size

The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

    from store import db, create_app
    db.create_all(app=create_app())
    quit()


Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from email.mime import image
from flask import Blueprint
from . import db
from .models import Category, Bracelet, Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    chainBracelet = Category(name='Chain Bracelets', image='brixham_mooring_silver.jpg')
    leatherBracelet = Category(name='Leather Bracelets', image='coal_black_cullen.jpg')
    stoneBracelet = Category(name='Stone Bracelets', image='blue_turquoise_mantaro.png')
      
    try:
        db.session.add(chainBracelet)
        db.session.add(leatherBracelet)
        db.session.add(stoneBracelet)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

    # xs = Size(sizename='XS', length='17cm')
    # s = Size(sizename='S', length='19cm')
    # m = Size(sizename='M', length='21cm')
    # l = Size(sizename='L', length='23cm')

    # try:
    #     db.session.add(xs)
    #     db.session.add(s)
    #     db.session.add(m)
    #     db.session.add(l)
    #     db.session.commit()
    # except:
    #     return 'There was an issue adding the sizes in dbseed function'

    bc1 = Bracelet(SKU='CB10001', name='Brisham Morring Silver', image='brixham_mooring_silver.jpg', price=105.00,\
        description='''The Brisham Morring Silver Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''',
         category_id=chainBracelet.id)

    bc2 = Bracelet(SKU='CB10002', name='Dundee Morning Silver', image='dundee_morning_silver.jpg', price=115.00,\
        description='''The Dundee Morning Silver Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''',
         category_id=chainBracelet.id)
    bc3 = Bracelet(SKU='CB10003', name='Lerwick Mooring Silver', image='lerwick_mooring_silver_chain.jpg', price=125.00,\
        description='''The Lerwick Mooring Silver Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''',
         category_id=chainBracelet.id)
    bc4 = Bracelet(SKU='CB10004', name='London Mooring Silver', image='london_mooring_silver_chain.jpg', price=135.00,\
        description='''The London Mooring Silver Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''',
         category_id=chainBracelet.id)
    bc5 = Bracelet(SKU='CB10005', name='Tyne Mooring Silver', image='Tyne-mooring-silver.jpg', price=135.00,\
        description='''The Tyne Mooring Silver Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''',
         category_id=chainBracelet.id)
    bc6 = Bracelet(SKU='CB10006', name='Tablot Mooring Silver', image='talbot_mooring_silver.jpg', price=145.00,\
        description='''The Tablot Mooring Silver Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''',
         category_id=chainBracelet.id)
    bc7 = Bracelet(SKU='CB10007', name='Padstow Mooring Silver', image='padstow_mooring_silver.jpg', price=155.00,\
        description='''The Padstow Mooring Silver Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''',
         category_id=chainBracelet.id)
    
    bl1 = Bracelet(SKU='CB20001', name='Coal Black Cullen', image='coal_black_cullen.jpg', price=115.00,\
        description='''The Coal Black Cullen Leather Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''', category_id=leatherBracelet.id)
    bl2 = Bracelet(SKU='CB20002', name='Coal Black Flyak', image='coal_black_flyak.jpg', price=135.00,\
        description='''The Coal Black Flyak Leather Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''', category_id=leatherBracelet.id)
    bl3 = Bracelet(SKU='CB20003', name='Midnight Black Alderney', image='midnight_black_alderney.jpg', price=155.00,\
        description='''The Midnight Black Alderney Leather Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''', category_id=leatherBracelet.id)
    bl4 = Bracelet(SKU='CB20004', name='Midnight Black Hayling', image='midnight_black_hayling.jpg', price=165.00,\
        description='''The Midnight Black Hayling Leather Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''', category_id=leatherBracelet.id)
    bl5 = Bracelet(SKU='CB20005', name='Midnight Black Jura', image='midnight_black_jura.jpg', price=170.00,\
        description='''The Midnight Black Jura Leather Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''', category_id=leatherBracelet.id)
    bl6 = Bracelet(SKU='CB20005', name='Midnight Black Skype', image='midnight_black_skype.jpg', price=180.00,\
        description='''The Midnight Black Skype Leather Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''', category_id=leatherBracelet.id)
   
    bs1 = Bracelet(SKU='CB30001', name='Blue Turquoise Tekapo', image='blue_turquoise_tekapo.jpg', price=215.00,\
        description='''The Blue Turquoise Tekapo Stone Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''', category_id=stoneBracelet.id)
    bs2 = Bracelet(SKU='CB30002', name='Blue Turquoise Mantaro', image='blue_turquoise_mantaro.jpg', price=225.00,\
        description='''The Blue Turquoise Mantaro Stone Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''', category_id=stoneBracelet.id)
    bs2 = Bracelet(SKU='CB30003', name='Brown Tigers Eye Atrato', image='brown_tigers_eye_atrato.png', price=235.00,\
        description='''The Brown Tigers Eye Atrato Stone Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''', category_id=stoneBracelet.id)
    bs3 = Bracelet(SKU='CB30003', name='Green Emerald Innot', image='green_emerald_innot.png', price=245.00,\
        description='''The Green Emerald Innot Stone Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''', category_id=stoneBracelet.id)
    bs4 = Bracelet(SKU='CB30004', name='Multicoloured Gem Mantaro', image='muticoloured_multi_gem_mantaro.png', price=245.00,\
        description='''The Multicoloured Gem Mantaro Stone Bracelet was created and handmade entirely in 
                                the United Kingdom by In Quality We Trust. Ra embraces an inquisitive existence and appreciates 
                                the Happy-Good Life for the Modern Journeyman (and woman). This Ra bracelet combines British 
                                handmade craftsmanship with a refined modern-minimalist aesthetic.''', category_id=stoneBracelet.id)
    try:
        db.session.add(bc1)
        db.session.add(bc2)
        db.session.add(bc3)
        db.session.add(bc4)
        db.session.add(bc5)
        db.session.add(bc6)
        db.session.add(bc7)
        db.session.add(bl1)
        db.session.add(bl2)
        db.session.add(bl3)
        db.session.add(bl4)
        db.session.add(bl5)
        db.session.add(bl6)
        db.session.add(bs1)
        db.session.add(bs2)
        db.session.add(bs3)
        db.session.add(bs4)
        db.session.commit()
    except:
        return 'There was an issue adding a bracelet in dbseed function'
    
    # statement = braceletinsizes.insert().values(bracelet_id=b1.id, size_id=xs.id)
    # statement = braceletinsizes.insert().values(bracelet_id=b1.id, size_id=s.id)
    # statement = braceletinsizes.insert().values(bracelet_id=b1.id, size_id=m.id)
    # statement = braceletinsizes.insert().values(bracelet_id=b1.id, size_id=l.id)

    #Brac1
    # brac1InSizeXS = braceletinsizes.insert().values(bracelet_id=b1.id, size_id=xs.id)
    # brac1InSizeS = braceletinsizes.insert().values(bracelet_id=b1.id, size_id=s.id)
    # brac1InSizeM = braceletinsizes.insert().values(bracelet_id=b1.id, size_id=m.id)
    # brac1InSizeL = braceletinsizes.insert().values(bracelet_id=b1.id, size_id=l.id)
    #Brac2
    # brac2InSizeXS = braceletinsizes.insert().values(bracelet_id=b2.id, size_id=xs.id)
    # brac2InSizeS = braceletinsizes.insert().values(bracelet_id=b2.id, size_id=s.id)
    # brac2InSizeM = braceletinsizes.insert().values(bracelet_id=b2.id, size_id=m.id)
    # brac2InSizeL = braceletinsizes.insert().values(bracelet_id=b2.id, size_id=l.id)
    #Brac3
    # brac3InSizeXS = braceletinsizes.insert().values(bracelet_id=b3.id, size_id=xs.id)
    # brac3InSizeS = braceletinsizes.insert().values(bracelet_id=b3.id, size_id=s.id)
    # brac3InSizeM = braceletinsizes.insert().values(bracelet_id=b3.id, size_id=m.id)
    # brac3InSizeL = braceletinsizes.insert().values(bracelet_id=b3.id, size_id=l.id)

    # try:
    #     db.session.execute(brac1InSizeXS)
    #     db.session.execute(brac1InSizeS)
    #     db.session.execute(brac1InSizeM)
    #     db.session.execute(brac1InSizeL)
    #     db.session.execute(brac2InSizeXS)
    #     db.session.execute(brac2InSizeS)
    #     db.session.execute(brac2InSizeM)
    #     db.session.execute(brac2InSizeL)
    #     db.session.execute(brac3InSizeXS)
    #     db.session.execute(brac3InSizeS)
    #     db.session.execute(brac3InSizeM)
    #     db.session.execute(brac3InSizeL)
    #     #db.session.execute(statement)
    #     db.session.commit()
    # except:
    #     return 'There was an issue adding the bracelets in size in dbseed function'

    return 'DATA LOADED'


