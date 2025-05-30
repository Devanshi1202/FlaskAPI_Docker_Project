from flask import Blueprint, request, jsonify
from app import mongo

main = Blueprint("main", __name__)

# Route: Get all users
@main.route("/users", methods=["GET"])
def get_users():
    users = list(mongo.db.users.find())
    for user in users:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string for JSON
    return jsonify(users), 200

# Route: Add a new user
@main.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    result = mongo.db.users.insert_one({"name": data["name"]})
    return jsonify({"id": str(result.inserted_id)}), 201

# Optional: Get a specific user by ID
@main.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    from bson.objectid import ObjectId
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return jsonify({"error": "User not found"}), 404
    user["_id"] = str(user["_id"])
    return jsonify(user), 200
