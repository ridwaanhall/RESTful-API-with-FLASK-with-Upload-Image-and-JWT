from app import app, response
from flask import request, jsonify, render_template
from app.controller import CustomerController, UserController
#from flask_jwt_extended import

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

@app.route('/')
def index():
    return 'Hello ridwaanhall'
    #return render_template('base.html')

@app.route("/protected", methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, "Success")

@app.route("/customers", methods=['GET', 'POST'])
def customers():
    if request.method == 'GET':
        return CustomerController.index()
    else:
        return CustomerController.save()

@app.route("/customers/<cust_id>", methods=['GET','PUT','DELETE'])
def customersDetail(cust_id):
    if request.method == 'GET':
        return CustomerController.detail(cust_id)
    elif request.method == 'PUT':
        return CustomerController.update(cust_id)
    else :
        return CustomerController.delete(cust_id)

@app.route("/createadmin", methods=['POST'])
def users():
    return UserController.buatAdmin()

@app.route("/login", methods=['POST'])
def logins():
    return UserController.login()

@app.route("/fileupload", methods=['POST'])
def uploads():
    return UserController.upload()