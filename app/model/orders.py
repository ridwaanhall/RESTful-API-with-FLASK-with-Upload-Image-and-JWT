from app import db
from datetime import datetime
from app.model.customers import Customers

class Orders(db.Model):
    order_num  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    cust_id    = db.Column(db.Integer, db.ForeignKey(Customers.cust_id))
    
    def __repr__(self):
        return '<Orders {}>'.format(self.name)