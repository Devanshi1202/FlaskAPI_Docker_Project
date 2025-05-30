from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

mongo = PyMongo()

def create_app(test_config=None):
    app = Flask(__name__)

    # Use environment variable or test config
    app.config["MONGO_URI"] = test_config.get("MONGO_URI") if test_config else os.environ.get("MONGO_URI", "mongodb://localhost:27017/testdb")

    mongo.init_app(app)

    @app.route('/users', methods=['POST'])
    def add_user():
        data = request.get_json()
        result = mongo.db.users.insert_one({
            'name': data['name'],
            'email': data['email']
        })
        return jsonify({'id': str(result.inserted_id)}), 201

    @app.route('/users', methods=['GET'])
    def get_users():
        users = []
        for user in mongo.db.users.find():
            users.append({
                'id': str(user['_id']),
                'name': user['name'],
                'email': user['email']
            })
        return jsonify(users)

    @app.route('/users/<user_id>', methods=['GET'])
    def get_user(user_id):
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            return jsonify({
                'id': str(user['_id']),
                'name': user['name'],
                'email': user['email']
            })
        return jsonify({'error': 'User not found'}), 404

    return app

# This is only used when running manually (not during unit tests)
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="127.0.0.1", port=5000)
