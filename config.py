import os

class Config:

    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://edu:kmox002localhost/pitches'


    UPLOADED_PHOTOS_DEST ='app/static/photos'

       #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch It Up!'
    SENDER_EMAIL = 'staremdee@gmail.com'

    @staticmethod
    def init_app(app):
        pass