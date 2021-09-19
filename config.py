import os

class Config:

    SECRET_KEY='edwin123456'
    SQLALCHEMY_DATABASE_URI ='postgres://nhbwrslngrtoki:97cb5457b6f0c49420740b499c0c5c3b6f8479d6db7817277a3ff2d8e211cc23@ec2-44-195-16-34.compute-1.amazonaws.com:5432/d5p6799he6jnc2'

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
    SQLALCHEMY_DATABASE_URI ='postgres://nhbwrslngrtoki:97cb5457b6f0c49420740b499c0c5c3b6f8479d6db7817277a3ff2d8e211cc23@ec2-44-195-16-34.compute-1.amazonaws.com:5432/d5p6799he6jnc2'

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
