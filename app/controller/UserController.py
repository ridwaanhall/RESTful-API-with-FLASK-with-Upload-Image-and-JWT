from app.model.user import User
from app import response, app, db, uploadconfig
from flask import request
from flask_jwt_extended import *
from datetime import datetime, timedelta

from app.model.images import Images
import os
import uuid
from werkzeug.utils import secure_filename

def upload():
    try:
        judul = request.form.get('judul')
        if 'file' not in request.files:
            return response.badRequest([], 'File tidak tersedia')
        file = request.files['file']
        if file.filename == '':
            return response.badRequest([], 'File tidak tersedia')
        if file and uploadconfig.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            uid = uuid.uuid4()
            renamefile = "Flask-" + str(uid)+"-"+filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            
            uploads = Images(judul=judul, pathname=renamefile)
            db.session.add(uploads)
            db.session.commit()
            return response.success(
                {
                    'judul' : judul,
                    'pathname' : renamefile,
                }, "Sukses upload file"
            )
        else:
            return response.badRequest([], 'File tidak diizinkan')
    except Exception as e:
        print(e)
        
def buatAdmin():
    try:
        name = request.form.get('name')
        email =request.form.get('email')
        password = request.form.get('password')
        level = 1

        #tampung pada sebuah variable
        users=User(name=name, email=email, level=level)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success('','Sukses menambah user')
    except Exception as e:
        print(e)

def singleObject(data):
    data={
        'id' : data.id,
        'name' : data.name,
        'email' : data.email,
        'level'  : data.level
    }
    return data

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user :
            return response.badRequest([],'Email tak terdaftar')
        if not user.checkPassword(password):
            return response.badRequest([],'Kombinasi password salah')
        data = singleObject(user)
        #token setelah login berapa lama
        expires = timedelta(minutes=2)
        expires_refresh= timedelta(minutes=2)
        #membuat akses token
        acces_token = create_access_token(data, fresh=True,expires_delta=expires)
        refresh_token = create_refresh_token(data,expires_delta=expires_refresh)
        return response.success({
            "data" : data,
            "access_token" : acces_token,
            "refresh_token" : refresh_token
        },"sukses login")
    except Exception as e:
        print(e)