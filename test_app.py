import os
import json
import unittest
from bson import ObjectId
from app import create_app, mongo

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            "MONGO_URI": os.environ.get("MONGO_URI", "mongodb://localhost:27017/testdb")
        })
        self.app.testing = True
        self.client = self.app.test_client()

        # Clean up before each test using app context
        with self.app.app_context():
            mongo.db.users.delete_many({})

    def tearDown(self):
        if mongo.cx:
            mongo.cx.close()

    def test_get_users(self):
        with self.app.app_context():
            mongo.db.users.insert_one({"name": "John Doe", "email": "john@example.com"})

        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_add_user(self):
        user_data = {"name": "Test User", "email": "test@example.com"}
        response = self.client.post(
            '/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.get_json())

    def test_get_user_not_found(self):
        fake_id = "000000000000000000000000"
        response = self.client.get(f'/users/{fake_id}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json().get("error"), "User not found")

if __name__ == '__main__':
    unittest.main()
