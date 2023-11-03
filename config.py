import os
DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))
# MEMBUAT CLASS OBJECT
class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    # koneksi ke SQLALCHEMY untuk koneksi
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    # mengatur track modifikasi apakah true/false 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    # JWT token
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    
    
    UPLOAD_FOLDER = str(os.environ.get("UPLOAD_FOLDER"))
    #UPLOAD_FOLDER = os.path.join(basedir, 'upload')  # Specify the correct folder path
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024