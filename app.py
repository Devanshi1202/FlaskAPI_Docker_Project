from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/testdb"
mongo = PyMongo(app)
users_collection = mongo.db.users


@app.route('/users', methods=['POST'])
def add_user():
    """
    Add a new user to the MongoDB collection.
    """
    data = request.get_json()
    result = users_collection.insert_one({
        'name': data['name'],
        'email': data['email']
    })
    return jsonify({'id': str(result.inserted_id)}), 201


@app.route('/users', methods=['GET'])
def get_users():
    """
    Retrieve all users from the MongoDB collection.
    """
    users = []
    for user in users_collection.find():
        users.append({
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email']
        })
    return jsonify(users)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieve a single user by ID from the MongoDB collection.
    """
    user = users_collection.find_one({'_id': ObjectId(user_id)})
    if user:
        return jsonify({
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email']
        })
    return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
