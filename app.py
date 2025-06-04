# import streamlit as st
# import openai
# import os
# from dotenv import load_dotenv

# # Load API key
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Streamlit setup
# st.set_page_config(page_title="Prenatal Care GPT Chatbot", page_icon="🤱", layout="wide")
# st.title("🤱 Personalized Prenatal Care Chatbot")
# st.markdown("Hello! I'm your AI prenatal care assistant. Ask me anything about pregnancy — symptoms, nutrition, or general wellness 💬")

# # Session state for chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "system", "content": (
#             "You are a professional prenatal care assistant. Provide empathetic, clear, and evidence-based guidance "
#             "to expecting mothers based on their symptoms, trimester, nutrition, or medical concerns. "
#             "Always be polite, warm, and supportive."
#             "If a query apart from prenatal care or pregnancy concerns is asked answer that you can answer quetions related to prenatal and pregnancy concerns only."
#         )}
#     ]

# # Show conversation history
# for msg in st.session_state.messages[1:]:  # skip system prompt
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # User input
# user_input = st.chat_input("Type your question here...")

# if user_input:
#     # Store user message
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Call OpenAI GPT API
#     with st.spinner("Thinking..."):
#         try:
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",  # or "gpt-4" if you have access
#                 messages=st.session_state.messages
#             )
#             assistant_reply = response["choices"][0]["message"]["content"]
#         except Exception as e:
#             assistant_reply = "Oops! Something went wrong. Please try again later."
#             st.error(str(e))

#     # Store assistant response
#     st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
#     with st.chat_message("assistant"):
#         st.markdown(assistant_reply)




#import streamlit as st
#import openai
#import os
#from dotenv import load_dotenv
#
## Load API key
#load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
#
## Load the prenatal care guide text
#with open("prenatal_care_guide.txt", "r", encoding="utf-8") as f:
#    guide_content = f.read()
#
## Streamlit setup
#st.set_page_config(page_title="Prenatal Care GPT Chatbot", page_icon="🤱", layout="wide")
#st.title("🤱 Personalized Prenatal Care Chatbot")
#st.markdown("Ask anything about pregnancy—nutrition, symptoms, exercises, trimester-specific care, and more!")
#
## Initialize chat history
#if "messages" not in st.session_state:
#    st.session_state.messages = [
#        {"role": "system", "content": (
#            "You are a professional prenatal care doctor. Provide medically accurate, empathetic, and evidence-based "
#            "You are a professional prenatal care assistant. Provide empathetic, clear, and evidence-based guidance "
#            "to expecting mothers based on their symptoms, trimester, nutrition, or medical concerns. "
#            "Always be polite, warm, and supportive. "
#            "If a query apart from prenatal care or pregnancy concerns is asked, respond that you can only answer questions related to prenatal and pregnancy concerns. "
#            f"Here is a reference guide you should use when answering questions:\n\n{guide_content}"
#        )}
#    ]
#
## Display past messages
#for msg in st.session_state.messages[1:]:
#    with st.chat_message(msg["role"]):
#        st.markdown(msg["content"])
#
## User input
#user_input = st.chat_input("How can I help you today?")
#
#if user_input:
#    st.session_state.messages.append({"role": "user", "content": user_input})
#    with st.chat_message("user"):
#        st.markdown(user_input)
#
#    # Call OpenAI
#    client = openai.OpenAI()
#
#    with st.spinner("Thinking..."):
#        try:
#            response = client.chat.completions.create(
#                model="gpt-3.5-turbo",
#                messages=st.session_state.messages
#            )
#            assistant_reply = response.choices[0].message.content
#        except Exception as e:
#            assistant_reply = "Sorry, something went wrong while contacting the model."
#            st.error(str(e))
#
#    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
#    with st.chat_message("assistant"):
#        st.markdown(assistant_reply)


#
#import streamlit as st
#import openai
#import os
#import pandas as pd
#from dotenv import load_dotenv
#
## Load API key
#load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
#
## Load prenatal care guide
#with open("prenatal_care_guide.txt", "r", encoding="utf-8") as f:
#    prenatal_guide = f.read()
#
## Load food dataset
#try:
#    food_df = pd.read_csv("food.csv")
#except Exception as e:
#    food_df = pd.DataFrame()
#    st.error(f"Failed to load food dataset: {e}")
#
## Streamlit UI setup
#st.set_page_config(page_title="Prenatal Care GPT Chatbot", page_icon="🤱", layout="wide")
#st.title("🤱 Personalized Prenatal Care Chatbot")
#st.markdown("Ask anything about pregnancy—nutrition, symptoms, trimester-specific care, or exercise!")
#
## Initialize chat history
#if "messages" not in st.session_state:
#    st.session_state.messages = [
#        {"role": "system", "content": (
#            "You are a highly experienced, board-certified OB-GYN specializing in prenatal care. "
#            "You provide accurate, warm, and empathetic advice to pregnant women based on their symptoms, stage of pregnancy, medical history, and emotional wellbeing. "
#            "Always explain things in a calm, easy-to-understand tone—like a doctor talking to a concerned patient during a consultation. "
#            "If asked questions outside pregnancy or prenatal care, gently remind them that you specialize only in this area.\n\n"
#            "Refer to the following prenatal guide when needed:\n\n"
#            f"{prenatal_guide}\n\n"
#            "Your goal is to make every mom-to-be feel heard, cared for, and confident."
#        )}
#    ]
#
#
## Show past conversation
#for msg in st.session_state.messages[1:]:  # skip system prompt
#    with st.chat_message(msg["role"]):
#        st.markdown(msg["content"])
#
## Food recommendation helper
#def recommend_foods(nutrient_keyword, trimester=None):
#    if food_df.empty:
#        return "Sorry, food data is not available at the moment."
#    
#    filtered = food_df[
#        food_df['nutrients'].str.contains(nutrient_keyword, case=False, na=False) &
#        food_df['safe_in_pregnancy'].str.lower().eq("yes")
#    ]
#
#    if filtered.empty:
#        return f"No foods found for {nutrient_keyword}."
#
#    top = filtered[["food_name", "nutrients"]].head(5)
#    recommendation = "**Here are some doctor-recommended foods:**\n"
#    for _, row in top.iterrows():
#        recommendation += f"- **{row['food_name']}** — Nutrients: *{row['nutrients']}*\n"
#    return recommendation
#
## Capture user input
#user_input = st.chat_input("Type your question here...")
#
#if user_input:
#    st.session_state.messages.append({"role": "user", "content": user_input})
#    with st.chat_message("user"):
#        st.markdown(user_input)
#
#    # Basic food-related keyword detection (you can make this smarter)
#    food_related_keywords = ["iron", "protein", "calcium", "vitamin", "zinc", "fiber"]
#    reply_generated = False
#
#    for keyword in food_related_keywords:
#        if keyword in user_input.lower():
#            st.session_state.messages.append({"role": "assistant", "content": recommend_foods(keyword)})
#            with st.chat_message("assistant"):
#                st.markdown(recommend_foods(keyword))
#            reply_generated = True
#            break
#
#    if not reply_generated:
#        # Call OpenAI API
#        client = openai.OpenAI()
#        with st.spinner("Thinking..."):
#            try:
#                response = client.chat.completions.create(
#                    model="gpt-3.5-turbo",
#                    messages=st.session_state.messages
#                )
#                assistant_reply = response.choices[0].message.content
#            except Exception as e:
#                assistant_reply = "Sorry, something went wrong while contacting the model."
#                st.error(str(e))
#
#        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
#        with st.chat_message("assistant"):
#            st.markdown(assistant_reply)






#import streamlit as st
#import openai
#import os
#from dotenv import load_dotenv
#from pymongo import MongoClient
#
## Connect to MongoDB (update URI as needed)
#client = MongoClient("mongodb://localhost:27017/")  # or your Mongo URI
#db = client["pregnocare"]
#users_collection = db["users"]
#
## Load environment variables
#load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
#
## Load prenatal care guide text
#with open("prenatal_care_guide.txt", "r", encoding="utf-8") as file:
#    prenatal_guide = file.read()
#
## Page config
#st.set_page_config(page_title="PregnoCare - Prenatal Chatbot", page_icon="🤰", layout="wide")
#
## Custom CSS for layout
#st.markdown("""
#    <style>
#    html, body, div, p, h1, h2, h3 {
#        font-family: 'Segoe UI', sans-serif !important;
#    }
#    .app-title {
#        text-align: center;
#        color: #00acc1;
#        font-size: 40px;
#        font-weight: bold;
#        padding-top: 30px;
#        padding-bottom: 10px;
#    }
#    .chat-container {
#        background-color: #1e1e1e;
#        padding: 2rem;
#        border-radius: 20px;
#        max-width: 900px;
#        margin: auto;
#        box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.05);
#    }
#    .message-user {
#        background-color: #2c2c2c;
#        padding: 1.2rem;
#        border-radius: 12px;
#        margin-bottom: 12px;
#        color: #ffffff;
#        font-size: 16px;
#        line-height: 1.6;
#    }
#    .message-assistant {
#        background-color: #00796b;
#        padding: 1.2rem;
#        border-radius: 12px;
#        margin-bottom: 12px;
#        color: #ffffff;
#        font-size: 16px;
#        line-height: 1.6;
#    }
#    .doctor-card {
#        background: #263238;
#        border-left: 6px solid #00acc1;
#        padding: 1.5rem;
#        border-radius: 15px;
#        color: #e0f2f1;
#        margin-bottom: 1.5rem;
#        font-size: 18px;
#        line-height: 1.6;
#    }
#    .stChatInput > div {
#        background-color: #121212;
#        border-radius: 10px;
#        font-size: 16px;
#    }
#    </style>
#""", unsafe_allow_html=True)
#
## App Title
#st.markdown("<div class='app-title'>👩‍⚕️ PregnoCare - Prenatal Care Specialist</div>", unsafe_allow_html=True)
#
## Start chat box
#st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
#
## Intro doctor card
#st.markdown(
#    "<div class='doctor-card'>"
#    "<h4>Welcome, I’m here to help guide you through your pregnancy journey — "
#    "feel free to ask anything about your health, diet, symptoms, or trimester care.</h4>"
#    "</div>", 
#    unsafe_allow_html=True
#)
#
## Initialize chat history
#if "messages" not in st.session_state:
#    st.session_state.messages = [
#        {"role": "system", "content": (
#            "You are a highly experienced, board-certified OB-GYN specializing in prenatal care. "
#            "You provide warm, doctor-like guidance to pregnant women. Always listen empathetically, "
#            "explain clearly, and answer using evidence-based medical knowledge. "
#            "If a question is unrelated to pregnancy or prenatal care, gently redirect them. "
#            "Use this prenatal care guide as reference:\n\n"
#            f"{prenatal_guide}"
#        )}
#    ]
#
## Display chat history
#for msg in st.session_state.messages[1:]:  # skip system message
#    role_class = "message-user" if msg["role"] == "user" else "message-assistant"
#    st.markdown(f"<div class='{role_class}'>{msg['content']}</div>", unsafe_allow_html=True)
#
## Chat input
#user_input = st.chat_input("Ask a question related to your pregnancy...")
#
#if user_input:
#    st.session_state.messages.append({"role": "user", "content": user_input})
#    st.markdown(f"<div class='message-user'>{user_input}</div>", unsafe_allow_html=True)
#
#    client = openai.OpenAI()
#
#    with st.spinner("Doctor is thinking..."):
#        try:
#            response = client.chat.completions.create(
#                model="gpt-4",  # or use "gpt-3.5-turbo"
#                messages=st.session_state.messages
#            )
#            reply = response.choices[0].message.content
#        except Exception as e:
#            reply = "Sorry, I ran into a technical issue. Please try again."
#            st.error(str(e))
#
#    st.session_state.messages.append({"role": "assistant", "content": reply})
#    st.markdown(f"<div class='message-assistant'>{reply}</div>", unsafe_allow_html=True)
#
#st.markdown("</div>", unsafe_allow_html=True)  # end chat container





    # import streamlit as st
    # import openai
    # import os
    # from dotenv import load_dotenv
    # from pymongo import MongoClient


    # load_dotenv()
    # openai.api_key = os.getenv("OPENAI_API_KEY")


    # mongo_uri = os.getenv("MONGODB_URI")
    # client = MongoClient(mongo_uri)
    # db = client["User"]
    # users_collection = db["User_Details"]


    # with open("prenatal_care_guide.txt", "r", encoding="utf-8") as file:
    #     prenatal_guide = file.read()


    # st.set_page_config(page_title="PregnoCare - Prenatal Chatbot", page_icon="🤰", layout="wide")


    # if "logged_in" not in st.session_state:
    #     st.session_state.logged_in = False
    #     st.session_state.user_name = ""
    #     st.session_state.is_guest = False


    # def get_user(userid, password):
    #     return users_collection.find_one({"user_id": userid, "password": password})


    # if not st.session_state.logged_in:
    #     st.title("🔐 PregnoCare Login")

    #     login_mode = st.radio("Select Login Method", ["Login with User ID", "Continue as Guest"])

    #     if login_mode == "Login with User ID":
    #         with st.form("login_form"):
    #             userid = st.text_input("User ID")
    #             password = st.text_input("Password", type="password")
    #             login_button = st.form_submit_button("Login")

    #         if login_button:
    #             user = get_user(userid, password)
    #             if user:
    #                 st.session_state.logged_in = True
    #                 st.session_state.user_name = user["user_id"]
    #                 st.session_state.is_guest = False
    #                 st.success(f"👋 Welcome, {user['user_id']}! Redirecting to PregnoCare...")
    #             else:
    #                 st.error("❌ Invalid credentials. Please try again.")

    #             st.rerun()

    #     elif login_mode == "Continue as Guest":
    #         if st.button("Enter Guest Mode"):
    #             st.session_state.logged_in = True
    #             st.session_state.user_name = "Guest User"
    #             st.session_state.is_guest = True
    #             st.info("🔓 Logged in as Guest. Limited access granted.")
    #             st.rerun()

    #     st.stop()



    # st.markdown("""
    #     <style>
    #     html, body, div, p, h1, h2, h3 {
    #         font-family: 'Segoe UI', sans-serif !important;
    #     }
    #     .app-title {
    #         text-align: center;
    #         color: #00acc1;
    #         font-size: 40px;
    #         font-weight: bold;
    #         padding-top: 30px;
    #         padding-bottom: 10px;
    #     }
    #     .chat-container {
    #         background-color: #1e1e1e;
    #         padding: 2rem;
    #         border-radius: 20px;
    #         max-width: 900px;
    #         margin: auto;
    #         box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.05);
    #     }
    #     .message-user {
    #         background-color: #2c2c2c;
    #         padding: 1.2rem;
    #         border-radius: 12px;
    #         margin-bottom: 12px;
    #         color: #ffffff;
    #         font-size: 16px;
    #         line-height: 1.6;
    #     }
    #     .message-assistant {
    #         background-color: #00796b;
    #         padding: 1.2rem;
    #         border-radius: 12px;
    #         margin-bottom: 12px;
    #         color: #ffffff;
    #         font-size: 16px;
    #         line-height: 1.6;
    #     }
    #     .doctor-card {
    #         background: #263238;
    #         border-left: 6px solid #00acc1;
    #         padding: 1.5rem;
    #         border-radius: 15px;
    #         color: #e0f2f1;
    #         margin-bottom: 1.5rem;
    #         font-size: 18px;
    #         line-height: 1.6;
    #     }
    #     .stChatInput > div {
    #         background-color: #121212;
    #         border-radius: 10px;
    #         font-size: 16px;
    #     }
    #     </style>
    # """, unsafe_allow_html=True)


    # st.markdown("<div class='app-title'>👩‍⚕️ PregnoCare - Prenatal Care Specialist</div>", unsafe_allow_html=True)


    # st.markdown("<div class='chat-container'>", unsafe_allow_html=True)


    # welcome_msg = (
    #     f"<div class='doctor-card'><h4>Hello {st.session_state.user_name}, "
    #     "I’m here to support your pregnancy journey. Feel free to ask anything related to symptoms, trimester care, or nutrition.</h4></div>"
    # )
    # st.markdown(welcome_msg, unsafe_allow_html=True)


    # if "messages" not in st.session_state:
    #     st.session_state.messages = [
    #         {"role": "system", "content": (
    #             "You are a highly experienced, board-certified OB-GYN specializing in prenatal care. "
    #             "You provide warm, doctor-like guidance to pregnant women. Always listen empathetically, "
    #             "explain clearly, and answer using evidence-based medical knowledge. "
    #             "If a question is unrelated to pregnancy or prenatal care, gently redirect them. "
    #             "Use this prenatal care guide as reference:\n\n"
    #             f"{prenatal_guide}"
    #         )}
    #     ]


    # for msg in st.session_state.messages[1:]:
    #     role_class = "message-user" if msg["role"] == "user" else "message-assistant"
    #     st.markdown(f"<div class='{role_class}'>{msg['content']}</div>", unsafe_allow_html=True)


    # user_input = st.chat_input("Ask a question related to your pregnancy...")

    # if user_input:
    #     st.session_state.messages.append({"role": "user", "content": user_input})
    #     st.markdown(f"<div class='message-user'>{user_input}</div>", unsafe_allow_html=True)

    #     client = openai.OpenAI()

    #     with st.spinner("Preparing your personalized care response..."):
    #         try:
    #             response = client.chat.completions.create(
    #                 model="gpt-4",
    #                 messages=st.session_state.messages
    #             )
    #             reply = response.choices[0].message.content
    #         except Exception as e:
    #             reply = "Sorry, I ran into a technical issue. Please try again."
    #             st.error(str(e))

    #     st.session_state.messages.append({"role": "assistant", "content": reply})
    #     st.markdown(f"<div class='message-assistant'>{reply}</div>", unsafe_allow_html=True)


    # st.markdown("</div>", unsafe_allow_html=True)

# import streamlit as st
# import openai
# import os
# from dotenv import load_dotenv
# from pymongo import MongoClient
# import pandas as pd

# # Load environment variables
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")
# mongo_uri = os.getenv("MONGODB_URI")

# client = MongoClient(mongo_uri)
# db = client["User"]
# users_collection = db["User_Details"]

# # Load prenatal guide
# with open("prenatal_care_guide.txt", "r", encoding="utf-8") as file:
#     prenatal_guide = file.read()

# # Load food dataset
# try:
#     food_df = pd.read_csv("pregnocare_food_dataset.csv")
# except Exception as e:
#     st.error(f"Failed to load food dataset: {e}")
#     food_df = pd.DataFrame()

# # Streamlit config
# st.set_page_config(page_title="PregnoCare - Prenatal Chatbot", page_icon="🤰", layout="wide")

# # Initialize session state
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
#     st.session_state.user_name = ""
#     st.session_state.is_guest = False

# def get_user(userid, password):
#     return users_collection.find_one({"user_id": userid, "password": password})

# # Login UI
# if not st.session_state.logged_in:
#     st.title("🔐 PregnoCare Login")
#     login_mode = st.radio("Select Login Method", ["Login with User ID", "Continue as Guest"])

#     if login_mode == "Login with User ID":
#         with st.form("login_form"):
#             userid = st.text_input("User ID")
#             password = st.text_input("Password", type="password")
#             login_button = st.form_submit_button("Login")

#         if login_button:
#             user = get_user(userid, password)
#             if user:
#                 st.session_state.logged_in = True
#                 st.session_state.user_name = user["user_id"]
#                 st.session_state.is_guest = False
#                 st.success(f"👋 Welcome, {user['user_id']}! Redirecting to PregnoCare...")
#             else:
#                 st.error("❌ Invalid credentials. Please try again.")
#             st.rerun()

#     elif login_mode == "Continue as Guest":
#         if st.button("Enter Guest Mode"):
#             st.session_state.logged_in = True
#             st.session_state.user_name = "Guest User"
#             st.session_state.is_guest = True
#             st.info("🔓 Logged in as Guest. Limited access granted.")
#             st.rerun()

#     st.stop()

# # Custom CSS styling
# st.markdown("""
#     <style>
#     html, body, div, p, h1, h2, h3 {
#         font-family: 'Segoe UI', sans-serif !important;
#     }
#     .app-title {
#         text-align: center;
#         color: #00acc1;
#         font-size: 40px;
#         font-weight: bold;
#         padding-top: 30px;
#         padding-bottom: 10px;
#     }
#     .chat-container {
#         background-color: #1e1e1e;
#         padding: 2rem;
#         border-radius: 20px;
#         max-width: 900px;
#         margin: auto;
#         box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.05);
#     }
#     .message-user {
#         background-color: #2c2c2c;
#         padding: 1.2rem;
#         border-radius: 12px;
#         margin-bottom: 12px;
#         color: #ffffff;
#         font-size: 16px;
#         line-height: 1.6;
#     }
#     .message-assistant {
#         background-color: #00796b;
#         padding: 1.2rem;
#         border-radius: 12px;
#         margin-bottom: 12px;
#         color: #ffffff;
#         font-size: 16px;
#         line-height: 1.6;
#     }
#     .doctor-card {
#         background: #263238;
#         border-left: 6px solid #00acc1;
#         padding: 1.5rem;
#         border-radius: 15px;
#         color: #e0f2f1;
#         margin-bottom: 1.5rem;
#         font-size: 18px;
#         line-height: 1.6;
#     }
#     .stChatInput > div {
#         background-color: #121212;
#         border-radius: 10px;
#         font-size: 16px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # UI Components
# st.markdown("<div class='app-title'>👩‍⚕️ PregnoCare - Prenatal Care Specialist</div>", unsafe_allow_html=True)
# st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# welcome_msg = (
#     f"<div class='doctor-card'><h4>Hello {st.session_state.user_name}, "
#     "I’m here to support your pregnancy journey. Feel free to ask anything related to symptoms, trimester care, or nutrition.</h4></div>"
# )
# st.markdown(welcome_msg, unsafe_allow_html=True)

# # Initialize chat messages
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "system", "content": (
#             "You are a highly experienced, board-certified OB-GYN specializing in prenatal care. "
#             "You provide warm, doctor-like guidance to pregnant women. Always listen empathetically, "
#             "explain clearly, and answer using evidence-based medical knowledge. "
#             "If a question is unrelated to pregnancy or prenatal care, gently redirect them. "
#             "Use this prenatal care guide as reference:\n\n"
#             f"{prenatal_guide}"
#         )}
#     ]

# # Display chat history
# for msg in st.session_state.messages[1:]:
#     role_class = "message-user" if msg["role"] == "user" else "message-assistant"
#     st.markdown(f"<div class='{role_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# # Food recommendation helper
# def get_food_recommendation(keyword):
#     if food_df.empty:
#         return "Sorry, food recommendation data is currently unavailable."
#     matches = food_df[
#         (food_df["nutrients"].str.contains(keyword, case=False, na=False)) &
#         (food_df["safe_in_pregnancy"].str.lower() == "yes")
#     ].head(5)
#     if matches.empty:
#         return f"No pregnancy-safe foods found rich in {keyword}."
#     response = f"Here are some pregnancy-safe foods rich in **{keyword}**:\n"
#     for _, row in matches.iterrows():
#         response += f"- **{row['food_name']}** ({row['category']}): {row['serving_suggestions']}\n"
#     return response

# # Handle chat input
# user_input = st.chat_input("Ask a question related to your pregnancy...")

# if user_input:
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     st.markdown(f"<div class='message-user'>{user_input}</div>", unsafe_allow_html=True)

#     food_keywords = ["iron", "calcium", "folic acid", "protein", "fiber", "vitamin", "zinc", "magnesium"]
#     found_keyword = False

#     for keyword in food_keywords:
#         if keyword in user_input.lower():
#             reply = get_food_recommendation(keyword)
#             found_keyword = True
#             break

#     if not found_keyword:
#         client = openai.OpenAI()
#         with st.spinner("Preparing your personalized care response..."):
#             try:
#                 response = client.chat.completions.create(
#                     model="gpt-4",
#                     messages=st.session_state.messages
#                 )
#                 reply = response.choices[0].message.content
#             except Exception as e:
#                 reply = "Sorry, I ran into a technical issue. Please try again."
#                 st.error(str(e))

#     st.session_state.messages.append({"role": "assistant", "content": reply})
#     st.markdown(f"<div class='message-assistant'>{reply}</div>", unsafe_allow_html=True)

# st.markdown("</div>", unsafe_allow_html=True)


import streamlit as st
import openai
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd
import bcrypt
import speech_recognition as sr
import random  

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
mongo_uri = os.getenv("MONGODB_URI")

# Initialize OpenAI client
openai_client = openai.OpenAI(api_key=openai_api_key)

# MongoDB connection
try:
    client = MongoClient(mongo_uri)
    db = client["User"]
    users_collection = db["User_Details"]
    client.server_info()  # Test the connection
except Exception as e:
    st.error(f"Failed to connect to MongoDB: {e}")
    st.stop()

# Load datasets
try:
    with open("prenatal_care_guide.txt", "r", encoding="utf-8") as file:
        prenatal_guide = file.read()
except FileNotFoundError:
    st.error("Prenatal care guide not found.")
    prenatal_guide = ""

try:
    food_df = pd.read_csv("pregnocare_food_dataset.csv")
except Exception as e:
    st.error(f"Failed to load food dataset: {e}")
    food_df = pd.DataFrame()

# User management functions
def create_user(userid, password, created_at):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users_collection.insert_one({"user_id": userid, "password": hashed, "created_at": created_at})

def check_password(password, hashed):
    if isinstance(hashed, str):
        hashed = hashed.encode('utf-8')
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    except ValueError:
        print(f"Invalid hash encountered: {hashed}")
        return False

def get_user(userid, password):
    if not userid or not password:
        return None
    user = users_collection.find_one({"user_id": userid.lower()})
    if user and check_password(password, user["password"]):
        return user
    return None

def get_user_context(user_id):
    user = users_collection.find_one({"user_id": user_id})
    if user:
        return f"User is in {user.get('trimester', 'unknown')} trimester, reports symptoms: {', '.join(user.get('symptoms', []))}"
    return ""

# Risk assessment
def assess_risk(symptoms, trimester):
    high_risk_symptoms = ["severe nausea", "bleeding", "severe headache"]
    if any(s in symptoms for s in high_risk_symptoms):
        return "Warning: Your symptoms may indicate a risk. Please consult a doctor."
    return "Your symptoms appear normal, but monitor them and consult a doctor if they worsen."

# Voice input
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening....")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10) 
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "Timeout: No speech detected. Please try again and speak clearly."
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError:
            return "Speech recognition service unavailable."
        
# Food recommendation helper
def get_food_recommendation(user_input, user_allergies=[]):
    if food_df.empty:
        return "Sorry, food recommendation data is unavailable."
    keywords = ["iron", "calcium", "folic acid", "protein", "fiber", "vitamin", "zinc", "magnesium"]
    matched_keywords = [k for k in keywords if k in user_input.lower()]
    if not matched_keywords:
        return "Please specify a nutrient (e.g., iron, calcium)."
    
    response = ""
    all_recommended_foods = set()  # Track recommended foods to avoid repetition across nutrients
    for keyword in matched_keywords:
        # Filter and clean the dataset
        matches = food_df[
            (food_df["nutrients"].str.contains(keyword, case=False, na=False)) &
            (food_df["safe_in_pregnancy"].str.lower() == "yes") &
            (~food_df["food_name"].isin(user_allergies))
        ].copy()
        
        # Remove numbers in parentheses from food_name for uniqueness
        matches.loc[:, 'cleaned_food_name'] = matches['food_name'].apply(
            lambda x: x[:x.rfind('(')].strip() if '(' in x and x.endswith(')') else x
        )
        
        if not matches.empty:
            # Remove duplicates based on cleaned_food_name and serving_suggestions
            matches = matches.drop_duplicates(subset=['cleaned_food_name', 'serving_suggestions'], keep='first')
            # Shuffle the unique matches
            matches = matches.sample(frac=1, random_state=None).reset_index(drop=True)
            # Select up to 5 unique foods not already recommended
            selected_matches = []
            for _, row in matches.iterrows():
                if len(selected_matches) < 5 and row['cleaned_food_name'] not in all_recommended_foods:
                    selected_matches.append(row)
                    all_recommended_foods.add(row['cleaned_food_name'])
            
            if selected_matches:
                response += f"Pregnancy-safe foods rich in {keyword}:\n"
                for row in selected_matches:
                    # Ensure each food item is on a new line
                    response += f"- {row['cleaned_food_name']}: {row['serving_suggestions']}\n"
                response += "\n"  # Add an extra newline between nutrient sections
    
    return response.strip() or f"No safe foods found for {', '.join(matched_keywords)}."

# Streamlit config
st.set_page_config(page_title="PregnoCare - Prenatal Chatbot", page_icon="🤰", layout="wide")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_name = ""
    st.session_state.is_guest = False
    st.session_state.messages = []

# Login UI
if not st.session_state.logged_in:
    st.title("🔐 PregnoCare Login")
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
                st.session_state.user_name = user["user_id"]
                st.session_state.is_guest = False
                st.success(f"👋 Welcome, {user['user_id']}! Redirecting to PregnoCare...")
            else:
                st.error("❌ Invalid credentials. Please try again.")
            st.rerun()

    elif login_mode == "Continue as Guest":
        if st.button("Enter Guest Mode"):
            st.session_state.logged_in = True
            st.session_state.user_name = "Guest User"
            st.session_state.is_guest = True
            st.info("🔓 Logged in as Guest. Limited access granted.")
            st.rerun()

    st.stop()

# Custom CSS styling
st.markdown("""
    <style>
    html, body, div, p, h1, h2, h3 {
        font-family: 'Segoe UI', sans-serif !important;
    }
    .app-title {
        text-align: center;
        color: #00acc1;
        font-size: 40px;
        font-weight: bold;
        padding-top: 30px;
        padding-bottom: 10px;
    }
    .chat-container {
        background-color: #1e1e1e;
        padding: 2rem;
        border-radius: 20px;
        max-width: 900px;
        margin: auto;
        box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.05);
    }
    .message-user {
        background-color: #2c2c2c;
        padding: 1.2rem;
        border-radius: 12px;
        margin-bottom: 12px;
        color: #ffffff;
        font-size: 16px;
        line-height: 1.6;
    }
    .message-assistant {
        background-color: #00796b;
        padding: 1.2rem;
        border-radius: 12px;
        margin-bottom: 12px;
        color: #ffffff;
        font-size: 16px;
        line-height: 1.6;
    }
    .doctor-card {
        background: #263238;
        border-left: 6px solid #00acc1;
        padding: 1.5rem;
        border-radius: 15px;
        color: #e0f2f1;
        margin-bottom: 1.5rem;
        font-size: 18px;
        line-height: 1.6;
    }
    .stChatInput > div {
        background-color: #121212;
        border-radius: 10px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# UI Components
st.markdown("<div class='app-title'>👩‍⚕️ PregnoCare - Prenatal Care Specialist</div>", unsafe_allow_html=True)
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# Welcome message with user profile input
welcome_msg = f"<div class='doctor-card'><h4>Hello {st.session_state.user_name}, I’m here to support your pregnancy journey. Please update your profile to get personalized advice.</h4></div>"
st.markdown(welcome_msg, unsafe_allow_html=True)

# Profile update form
if not st.session_state.is_guest:
    with st.form("profile_form"):
        trimester = st.selectbox("Trimester", ["First", "Second", "Third"])
        symptoms = st.multiselect("Symptoms", ["Nausea", "Fatigue", "Back Pain", "Severe Nausea", "Bleeding", "Severe Headache"])
        allergies = st.text_input("Allergies (comma-separated)")
        profile_button = st.form_submit_button("Update Profile")
        if profile_button:
            users_collection.update_one(
                {"user_id": st.session_state.user_name},
                {"$set": {"trimester": trimester.lower(), "symptoms": symptoms, "allergies": allergies.split(",") if allergies else []}},
                upsert=True
            )
            st.success("Profile updated!")

# Initialize chat messages
if not st.session_state.messages:
    user_context = get_user_context(st.session_state.user_name)
    st.session_state.messages = [
        {"role": "system", "content": (
            "You are a highly experienced, board-certified OB-GYN specializing in prenatal care. "
            "You provide warm, doctor-like guidance to pregnant women. Always listen empathetically, "
            "explain clearly, and answer using evidence-based medical knowledge. "
            f"If a question is unrelated to pregnancy or prenatal care, gently redirect them. "
            f"Use this prenatal care guide as reference:\n\n{prenatal_guide}\n\n{user_context}"
        )}
    ]

# Display chat history
for msg in st.session_state.messages[1:]:
    role_class = "message-user" if msg["role"] == "user" else "message-assistant"
    st.markdown(f"<div class='{role_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# Handle chat input
user_input = st.chat_input("Ask a question related to your pregnancy...")
if st.button("Use Voice Input"):
    user_input = speech_to_text()

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f"<div class='message-user'>{user_input}</div>", unsafe_allow_html=True)

    # Check user profile for risk assessment
    user = users_collection.find_one({"user_id": st.session_state.user_name})
    if user and "symptoms" in user:
        risk_message = assess_risk(user["symptoms"], user.get("trimester", "unknown"))
        st.warning(risk_message)

    # Food recommendation
    food_keywords = ["iron", "calcium", "folic acid", "protein", "fiber", "vitamin", "zinc", "magnesium"]
    found_keyword = False
    allergies = user.get("allergies", []) if user else []

    for keyword in food_keywords:
        if keyword in user_input.lower():
            reply = get_food_recommendation(user_input, allergies)
            found_keyword = True
            break

    # OpenAI response
    if not found_keyword:
        with st.spinner("Preparing your personalized care response..."):
            try:
                response = openai_client.chat.completions.create(
                    model="gpt-4",
                    messages=st.session_state.messages
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = "Sorry, I ran into a technical issue. Please try again."
                st.error(str(e))

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.markdown(f"<div class='message-assistant'>{reply}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)