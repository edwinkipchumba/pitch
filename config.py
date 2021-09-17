import os

class Config:

    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://edu:kmox002localhost/pitches'


    UPLOADED_PHOTOS_DEST ='app/static/photos'