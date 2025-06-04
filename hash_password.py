from pymongo import MongoClient
import os
import bcrypt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
mongo_uri = os.getenv("MONGODB_URI")

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client["User"]
users_collection = db["User_Details"]

user_data = [
    {"user_id": "ab84", "password": "Pass@2656", "created_at": "21/03/2025"},
    {"user_id": "cd29", "password": "Pass@7291", "created_at": "02/04/2025"},
    {"user_id": "ef56", "password": "Pass@3107", "created_at": "05/04/2025"},
    {"user_id": "gh81", "password": "Pass@8510", "created_at": "06/03/2025"},
    {"user_id": "ij11", "password": "Pass@7207", "created_at": "17/03/2025"},
    {"user_id": "kl90", "password": "Pass@8296", "created_at": "05/03/2025"},
    {"user_id": "mn66", "password": "Pass@7572", "created_at": "03/03/2025"},
    {"user_id": "op21", "password": "Pass@3138", "created_at": "08/04/2025"},
    {"user_id": "qr49", "password": "Pass@5895", "created_at": "28/03/2025"},
    {"user_id": "st28", "password": "Pass@8100", "created_at": "26/03/2025"}
]

# Update each user's password with a bcrypt hash
for user in user_data:
    user_id = user["user_id"]
    plaintext_password = user["password"]
    hashed_password = bcrypt.hashpw(plaintext_password.encode('utf-8'), bcrypt.gensalt())
    users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"password": hashed_password}},
        upsert=True
    )
    print(f"Updated user {user_id} with hashed password: {hashed_password}")

print("Password hashing completed!")