
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
    if (database_name=="capstonedatabase" or database_name=="capstonedb_test"):
        database_path = "postgresql://{}/{}".format('localhost:5432', database_name)
    else:
        database_path ="postgres://dkxjzuwemchfll:aaf9007881331f576430a7f97e26eac04039dabbf3e00a4b8d12fe5da854c98a@ec2-35-170-85-206.compute-1.amazonaws.com:5432/dadk509idqbti2"
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
