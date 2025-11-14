import os

class Config:
    SECRET_KEY = 'bbb701908406488117ddc1acc269fe3eccb57ceb583c4f01a4e701671ee25ce3'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'ashabk@2351'
    MYSQL_DB = 'lostfound'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}