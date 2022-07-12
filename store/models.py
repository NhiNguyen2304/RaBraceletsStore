from . import db

class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    image = db.Column(db.String(60))

    def __repr__(self):
        str = "Id: {}, Name: {}\n" 
        str =str.format( self.id, self.name)
        return str

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('bracelet_id',db.Integer,db.ForeignKey('bracelets.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'bracelet_id') )

class Bracelet(db.Model):
    __tablename__='bracelets'
    id = db.Column(db.Integer, primary_key=True)
    SKU = db.Column(db.String(64),nullable=False)
    name = db.Column(db.String(64),nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    #sizes = db.relationship("Size", secondary=braceletinsizes, backref="bracelets")

    def __repr__(self):
        str = "Id: {}, SKU: {}, Name: {}, Price: {}, Description: {}, Image: {}, Category: {}\n" 
        str =str.format( self.id, self.SKU, self.name, self.price, self.description,self.image, self.category_id)
        return str

class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    status = db.Column(db.Boolean, default=False)
    totalprice = db.Column(db.Float)
    date = db.Column(db.DateTime)
    bracelets = db.relationship("Bracelet", secondary=orderdetails, backref="orders")

    def __repr__(self):
        str = "id: {}, Firstname: {}, Phone: {}, Status: {}, Total Cost: {}, Date: {}\n" 
        str =str.format( self.id, self.username, self.address, self.phone, self.status, self.totalprice, self.date)
        return str
