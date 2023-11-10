# config.py
from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevConfig(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABSE_URL', 'postgresql://postgres:secret@localhost:5432/boilerdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
