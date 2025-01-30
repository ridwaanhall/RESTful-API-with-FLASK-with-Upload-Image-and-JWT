import os
DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    
    
    UPLOAD_FOLDER = str(os.environ.get("UPLOAD_FOLDER"))

    MAX_CONTENT_LENGTH = 2 * 1024 * 1024