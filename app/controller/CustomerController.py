from array import array
from app.model import customers
from app.model.customers import Customers
from app.model.orders import Orders
from app import response, app, db
from flask import request

def index():
    try:
        customers = Customers.query.all()
        data      = formatarray(customers)
        return response.success(data, "Success")
    except Exception as e:
        print(e)
        
def formatarray(datas):
    array = []
    for i in datas:
        array.append(singleObject(i))
    return array

def singleObject(data):
    data = {
        'cust_id'      : data.cust_id,
        'cust_name'    : data.cust_name,
        'cust_address' : data.cust_address,
        'cust_city'    : data.cust_city,
        'cust_state'   : data.cust_state,
        'cust_zip'     : data.cust_zip,
        'cust_country' : data.cust_country,
        'cust_telp'    : data.cust_telp
        
    }
    return data

def detail(cust_id):
    try:
        customers = Customers.query.filter_by(cust_id=cust_id).first()
        orders = Orders.query.filter_by(cust_id=cust_id)
        if not customers:
            return response.badRequest([], 'Tidak ada data Customers')
        
        dataorders = formatOrders(orders)
        data = singleDetailOrders(customers, dataorders)
        
        return response.success(data, "Success")
    except Exception as e:
        return response.error(str(e))


def singleOrders(orders):
    data = {
        'order_num'  : orders.order_num,
        'order_date' : orders.order_date
    }
    return data

def formatOrders(data):
    array =[]
    for i in data:
        array.append(singleOrders(i))
    return array

# menampilkan data customers dan datanya order siapa aja
def singleDetailOrders(customers, orders):
    data = {
        'cust_id'      : customers.cust_id,
        'cust_name'    : customers.cust_name,
        'cust_address' : customers.cust_address,
        'cust_city'    : customers.cust_city,
        'cust_state'   : customers.cust_state,
        'cust_zip'     : customers.cust_zip,
        'cust_country' : customers.cust_country,
        'cust_telp'    : customers.cust_telp,
        # bentuk nested js
        'orders'       : orders
    }
    return data

def save():
    try:
        cust_id      = request.form.get('cust_id')
        cust_name    = request.form.get('cust_name')
        cust_address = request.form.get('cust_address')
        cust_city    = request.form.get('cust_city')
        cust_state   = request.form.get('cust_state')
        cust_zip     = request.form.get('cust_zip')
        cust_country = request.form.get('cust_country')
        cust_telp    = request.form.get('cust_telp')
        
        #Tampung pada sebuah variable
        saveCustomers = Customers(cust_id=cust_id, cust_name = cust_name, cust_address=cust_address, cust_city=cust_city, cust_state=cust_state, cust_zip=cust_zip, cust_country=cust_country, cust_telp=cust_telp)
        
        db.session.add(saveCustomers)
        db.session.commit()
        
        return response.success('', 'Sukses menambah data Customer')
    except Exception as e:
      print(e)
      
def update(cust_id):
    try:
        cust_name    = request.form.get('cust_name')
        cust_address = request.form.get('cust_address')
        cust_city    = request.form.get('cust_city')
        cust_zip     = request.form.get('cust_zip')
        cust_country = request.form.get('cust_country')
        cust_telp    = request.form.get('cust_telp')
        input = {
            'cust_name'    : cust_name,
            'cust_address' : cust_address,
            'cust_city'    : cust_city,
            'cust_zip'     : cust_zip,
            'cust_country' : cust_country,
            'cust_telp'    : cust_telp
        }
        customers = Customers.query.filter_by(cust_id=cust_id).first()
        customers.cust_name    = cust_name,
        customers.cust_address = cust_address,
        customers.cust_city    = cust_city,
        customers.cust_zip     = cust_zip,
        customers.cust_country = cust_country,
        customers.cust_telp    = cust_telp
        db.session.commit()
        return response.success(input, 'Sukses update data')
    except Exception as e:
        print(e)
        
def delete(cust_id):
    try:
        customers = Customers.query.filter_by(cust_id=cust_id).first()
        if not customers:
            return response.badRequest([],'data customers kosong...')
        db.session.delete(customers)
        db.session.commit()
        return response.success('','berhasil menghapus data customers')
    except Exception as e:
        print(e)