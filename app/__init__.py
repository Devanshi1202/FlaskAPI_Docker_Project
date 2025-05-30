import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app(test_config=None):
    app = Flask(__name__)
    
    # Configure MongoDB URI
    app.config["MONGO_URI"] = (
        test_config.get("MONGO_URI")
        if test_config
        else os.getenv("MONGO_URI", "mongodb://localhost:27017/testdb")
    )
    
    mongo.init_app(app)

    # Define routes here since there's no routes.py
    @app.route('/users', methods=['GET'])
    def get_users():
        users_collection = mongo.db.users
        users = list(users_collection.find({}, {'_id': 0}))
        return jsonify(users), 200

    @app.route('/users', methods=['POST'])
    def add_user():
        users_collection = mongo.db.users
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON body"}), 400
        users_collection.insert_one(data)
        return jsonify({"message": "User added successfully"}), 201

    return app
