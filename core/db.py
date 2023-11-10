from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:secret@localhost:5432/boilerdb", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

db = SQLAlchemy()
