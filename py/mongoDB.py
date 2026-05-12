from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId  
from dotenv import load_dotenv
import os

load_dotenv()       

mongo_uri = os.getenv("MONGODB_ATLAS_URI")

class DatabaseManager:
    def __init__(self):
        self.client = MongoClient(mongo_uri)
        self.db = self.client["python_bootcamp_db"]
        self.collection = self.db["users"]

    def create_user(self, name, email):
        user = {
            "name": name,
            "email": email,
            "created_at": datetime.utcnow()
        }
        result = self.collection.insert_one(user)
        print(f"User created with ID: {result.inserted_id}")

    def get_user(self, user_id):
        user = self.collection.find_one({"_id": ObjectId(user_id)})
        if user:
            print(f"User found: {user}")
        else:
            print("User not found.")

    def update_user(self, user_id, name=None, email=None):
        update_fields = {}
        if name:
            update_fields["name"] = name
        if email:
            update_fields["email"] = email
        
        if update_fields:
            result = self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_fields})
            if result.modified_count > 0:
                print("User updated successfully.")
            else:
                print("No changes made to the user.")
        else:
            print("No fields to update.")

    def delete_user(self, user_id):
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count > 0:
            print("User deleted successfully.")
        else:
            print("User not found.")

    @staticmethod
    def main():
        db_manager = DatabaseManager()
        
        while True:
            print("\nMenu:")
            print("1. Create User")
            print("2. Get User")
            print("3. Update User")
            print("4. Delete User")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                name = input("Enter name: ")
                email = input("Enter email: ")
                db_manager.create_user(name, email)
            
            elif choice == '2':
                user_id = input("Enter user ID: ")
                db_manager.get_user(user_id)
            
            elif choice == '3':
                user_id = input("Enter user ID: ")
                name = input("Enter new name (leave blank to skip): ")
                email = input("Enter new email (leave blank to skip
