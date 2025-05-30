from flask import Blueprint, request, jsonify
from app import mongo

main = Blueprint("main", __name__)

@main.route("/users", methods=["GET"])
def get_users():
    users = list(mongo.db.users.find())
    return jsonify(users), 200

@main.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    result = mongo.db.users.insert_one({"name": data["name"]})
    return jsonify({"id": str(result.inserted_id)}), 201
