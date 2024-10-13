# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('cosiek')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Kanapka#123@localhost/recipeappdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False