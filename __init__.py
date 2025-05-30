import os
from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # Use MONGO_URI from environment or default to localhost
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017")

    mongo.init_app(app)

    from .routes import main  # or whatever your blueprint is
    app.register_blueprint(main)

    return app
