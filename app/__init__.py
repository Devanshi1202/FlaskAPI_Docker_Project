import os
from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app(test_config=None):
    app = Flask(__name__)

    default_mongo_uri = "mongodb://localhost:27017/testdb"
    app.config["MONGO_URI"] = (
        test_config.get("MONGO_URI")
        if test_config and "MONGO_URI" in test_config
        else os.getenv("MONGO_URI", default_mongo_uri)
    )

    mongo.init_app(app)

    # Register your blueprint inside the function
    from app.routes import main
    app.register_blueprint(main)

    return app
