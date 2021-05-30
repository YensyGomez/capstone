import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  # CORS Headers
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
      return response
      
  @app.route('/')
  def get_greeting():
      excited = os.environ.get('EXCITED')
      if not excited:
         excited = 'true'
      greeting = "Hello Actors"
      if excited == 'true': greeting = greeting + "!!!!!"
      return greeting
      
  return app
APP = create_app()
if __name__ == '__main__':
    APP.run()
