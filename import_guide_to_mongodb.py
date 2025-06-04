import os
import json
import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI
mongo_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")

# Connect to MongoDB
try:
    client = MongoClient(mongo_uri)
    client.server_info()  # Test connection
    db = client["pregnocare"]
    guidelines_collection = db["guidelines"]
except Exception as e:
    st.error(f"Failed to connect to MongoDB: {e}")
    st.stop()

# Load and insert JSON
try:
    json_path = os.path.join(os.path.dirname(__file__), "prenatal_care_guide.json")
    with open(json_path, "r") as file:
        guide_data = json.load(file)
    guidelines_collection.insert_one(guide_data)
    st.success("Prenatal care guide imported to MongoDB successfully!")
except FileNotFoundError:
    st.error(f"Error: 'prenatal_care_guide.json' not found in {os.path.dirname(__file__)}. Please create the file.")
    st.stop()
except json.JSONDecodeError:
    st.error("Error: Invalid JSON format in 'prenatal_care_guide1.json'. Please check the file.")
    st.stop()
except Exception as e:
    st.error(f"Error: Failed to import guide to MongoDB: {e}")
    st.stop()