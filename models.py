
import os
from sqlalchemy import Column, String, Integer, Date, create_engine
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import json
#Sfrom flask_migrate import Migrate

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_name="capstonedatabase"):
    #database_path ="postgres://syyecrbfpbipfe:7a3a96cc18215d074d58db31d4c037d71d0a21de8029a9cc979455e7eba3008d@ec2-3-211-37-117.compute-1.amazonaws.com:5432/db08i5uuf21l1v"
    database_path = "postgresql://{}/{}".format('localhost:5432', database_name)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

'''
Movie
'''
class Movie(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = Column(Date)


  def __init__(self, title, release_date):
    self.title= title
    self.release_date = release_date

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date,
    }

'''
Actor
'''
class Actors(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender,
    }
