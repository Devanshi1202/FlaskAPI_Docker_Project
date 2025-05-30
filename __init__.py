# app/__init__.py
import os
from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["MONGO_URI"] = test_config.get("MONGO_URI") if test_config else os.environ.get("MONGO_URI", "mongodb://localhost:27017/testdb")
    
    mongo.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
