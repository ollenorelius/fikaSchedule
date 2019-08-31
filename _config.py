import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some stuff'
    EMAIL_SENDER = "email"
    EMAIL_PW = "password"
    HOST = "localhost:5000"