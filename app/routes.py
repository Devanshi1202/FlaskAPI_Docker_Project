from flask import Blueprint, jsonify, request
from app import mongo

main = Blueprint("main", __name__)

@main.route("/users", methods=["GET"])
def get_users():
    users = list(mongo.db.users.find())
    return jsonify(users), 200

@main.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Missing user data"}), 400
    result = mongo.db.users.insert_one({"name": data["name"]})
    return jsonify({"id": str(result.inserted_id)}), 201
