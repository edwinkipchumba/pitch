import os

class Config:

    SECRET_KEY='SECRET_KEY'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://edu:kmox002@localhost/pitches'

    #  image uploader
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
  

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://edu:kmox002@localhost/pitches_test'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # connecting to database
    # SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://edu:kmox002@localhost/pitches'
    

    DEBUG = True

         # connecting to Gmail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'PickUp!'
    SENDER_EMAIL = 'edwinkolem5@gmail.com'

  # editor
class Config:
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


    @staticmethod
    def init_app(app):
        pass

  

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
