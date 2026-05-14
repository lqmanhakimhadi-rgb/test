from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
import certifi

# Load environment variables
load_dotenv()

mongo_uri = os.getenv("MONGODB_ATLAS_URI")



class DatabaseManager:

    def __init__(self, db_name="example_db", connection_string=mongo_uri):

        self.client = MongoClient(
            connection_string,
            tls=True,
            tlsCAFile=certifi.where()
)

        self.db = self.client[db_name]

        self.users_collection = self.db.users

        self.posts_collection = self.db.posts

        self.init_database()

    def init_database(self):

        # Create unique index for email
        self.users_collection.create_index(
            "email",
            unique=True
        )

        # Create index for posts
        self.posts_collection.create_index(
            "user_id"
        )

    def create_user(self, name, email, age):

        try:

            user_doc = {
                "name": name,
                "email": email,
                "age": age,
                "created_at": datetime.now()
            }

            result = self.users_collection.insert_one(user_doc)

            return str(result.inserted_id)

        except Exception as e:

            print(f"Error: {e}")

            return None

    def create_post(self, user_id, title, content):

        try:

            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id

            post_doc = {
                "user_id": user_object_id,
                "title": title,
                "content": content,
                "created_at": datetime.now()
            }

            result = self.posts_collection.insert_one(post_doc)

            return str(result.inserted_id)

        except Exception as e:

            print(f"Error creating post: {e}")

            return None

    def get_all_users(self):

        try:

            users = list(self.users_collection.find())

            for user in users:
                user["_id"] = str(user["_id"])

            return users

        except Exception as e:

            print(f"Error fetching users: {e}")

            return []

    def get_user_posts(self, user_id):

        try:

            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id

            posts = list(
                self.posts_collection.find(
                    {"user_id": user_object_id}
                ).sort("created_at", -1)
            )

            for post in posts:
                post["_id"] = str(post["_id"])
                post["user_id"] = str(post["user_id"])

            return posts

        except Exception as e:

            print(f"Error fetching posts: {e}")

            return []

    def delete_user(self, user_id):

        try:

            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id

            # Delete related posts
            self.posts_collection.delete_many(
                {"user_id": user_object_id}
            )

            # Delete user
            result = self.users_collection.delete_one(
                {"_id": user_object_id}
            )

            return result.deleted_count > 0

        except Exception as e:

            print(f"Error deleting user: {e}")

            return False

    def close_connection(self):

        self.client.close()


def display_menu():

    print("\n" + "=" * 40)

    print("DATABASE MANAGER")

    print("=" * 40)

    print("1. Create User")
    print("2. View All Users")
    print("3. Create Post")
    print("4. View User Posts")
    print("5. Delete User")
    print("6. Exit")

    print("=" * 40)


def main():

    try:

        db = DatabaseManager()

        print("Connected to MongoDB successfully!")

    except Exception as e:

        print(f"Failed to connect to MongoDB: {e}")

        return

    while True:

        display_menu()

        choice = input("Enter your choice (1-6): ").strip()

        # Create User
        if choice == "1":

            print("\n--- Create New User ---")

            name = input("Enter name: ").strip()

            email = input("Enter email: ").strip()

            try:

                age = int(input("Enter age: ").strip())

                user_id = db.create_user(name, email, age)

                if user_id:

                    print(f"User created successfully! ID: {user_id}")

                else:

                    print("Failed to create user")

            except ValueError:

                print("Invalid age")

        # View Users
        elif choice == "2":

            print("\n--- All Users ---")

            users = db.get_all_users()

            if users:

                for user in users:

                    print(f"ID: {user['_id']}")
                    print(f"Name: {user['name']}")
                    print(f"Email: {user['email']}")
                    print(f"Age: {user['age']}")

            else:

                print("No users found")

        # Create Post
        elif choice == "3":

            print("\n--- Create New Post ---")

            user_id = input("Enter user ID: ").strip()

            title = input("Enter post title: ").strip()

            content = input("Enter post content: ").strip()

            post_id = db.create_post(user_id, title, content)

            if post_id:

                print(f"Post created successfully! ID: {post_id}")

            else:

                print("Failed to create post")

        # View User Posts
        elif choice == "4":

            print("\n--- View User Posts ---")

            user_id = input("Enter user ID: ").strip()

            posts = db.get_user_posts(user_id)

            if posts:

                for post in posts:

                    print(f"\nID: {post['_id']}")
                    print(f"Title: {post['title']}")
                    print(f"Content: {post['content']}")
                    print(f"Created: {post['created_at']}")

            else:

                print("No posts found")

        # Delete User
        elif choice == "5":

            print("\n--- Delete User ---")

            user_id = input("Enter user ID to delete: ").strip()

            confirm = input(
                f"Are you sure you want to delete user {user_id}? (y/n): "
            ).lower()

            if confirm == "y":

                if db.delete_user(user_id):

                    print("User deleted successfully")

                else:

                    print("User not found or deletion failed")

        # Exit
        elif choice == "6":

            print("\nClosing connection...")

            db.close_connection()

            print("Goodbye!")

            break

        # Invalid
        else:

            print("Invalid choice. Please enter 1-6")


if __name__ == "__main__":

    main()