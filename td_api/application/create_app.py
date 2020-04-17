from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import time

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_URL = os.environ['POSTGRES_URL']
POSTGRES_DB = os.environ['POSTGRES_DB']

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.Config')
    
    DB_URL = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(user=POSTGRES_USER,pw=POSTGRES_PASSWORD,url=POSTGRES_URL,db=POSTGRES_DB)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        from oauth2.routes import oauth2_routes
        from options.routes import options_routes

        # Register blueprints
        app.register_blueprint(oauth2_routes)
        app.register_blueprint(options_routes)
            
        # Connect to DB
        tries = 1
        while tries <= 5:
            try:
                print(f"\n========== DB CONNECTION ATTEMPT {tries}========== ")
                db.init_app(app)
                # Create tables for our models
                db.create_all()
                break
            except Exception as e:
                print("\n========== DB CONNECTION FAILED ========== ")
                print(f"\n========== Errors ========== ")
                print(e)
                time.sleep(1)
                tries += 1
        print("\n========== DB CONNECTED ========== ")

        return app
