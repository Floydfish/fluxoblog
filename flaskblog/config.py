import os

class Config:
    SECRET_KEY = os.environ.get('SCRT_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DB_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
