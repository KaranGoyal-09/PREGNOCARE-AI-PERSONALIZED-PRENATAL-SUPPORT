import streamlit as st
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["pregnocare"]
users_collection = db["users"]

# Function to check user

def get_user(userid, password):
    return users_collection.find_one({"userid": userid, "password": password})

def login():
    st.title("\U0001F510 PregnoCare Login")

    login_mode = st.radio("Select Login Method", ["Login with User ID", "Continue as Guest"])

    if login_mode == "Login with User ID":
        with st.form("login_form"):
            userid = st.text_input("User ID")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")

        if login_button:
            user = get_user(userid, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.user_name = user["name"]
                st.session_state.is_guest = False
                st.success(f"\U0001F44B Welcome, {user['name']}! Redirecting to PregnoCare...")
                st.rerun()
            else:
                st.error("\u274C Invalid credentials. Please try again.")

    elif login_mode == "Continue as Guest":
        if st.button("Enter Guest Mode"):
            st.session_state.logged_in = True
            st.session_state.user_name = "Guest User"
            st.session_state.is_guest = True
            st.info("\U0001F513 Logged in as Guest. Limited access granted.")
            st.rerun()
