import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    '''
        Set config variables for the flas app
        using Environment variables where available.
        Otherwise, create the config variable if not done already.
    '''
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET KEY') or 'Ryan will never get access to my CSS'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False

