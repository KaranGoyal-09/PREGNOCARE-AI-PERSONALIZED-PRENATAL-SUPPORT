# 🤰 PregnoCare AI

**PregnoCare AI** is a smart prenatal care assistant that offers personalized, AI-powered pregnancy support. Built using **Streamlit**, **OpenAI's GPT-4**, and **MongoDB**, the chatbot assists expecting mothers with dietary advice, risk detection based on symptoms, and answers to pregnancy-related questions — all in a doctor-like, conversational tone.

---

## 📌 About the Project

Many pregnant women do not have regular access to professional medical guidance, especially in rural or underserved areas. Traditional prenatal care systems are often generic, missing the nuances of individual health, trimester-specific symptoms, and dietary restrictions.

**PregnoCare AI** addresses this gap with:
- A chatbot trained on detailed pregnancy knowledge
- Nutritional recommendations personalized by trimester, allergies, and health conditions
- Empathetic responses simulating a doctor’s tone
- Symptom-based risk detection for early alerts

---

## 🎯 Project Aim

The goal is to:
- Deliver personalized prenatal care using AI and NLP
- Act as a **virtual assistant** and **companion** during pregnancy
- Help **educate and guide** mothers with contextual health suggestions
- Bridge the healthcare gap through an **accessible AI platform**

---

## 🌍 Impact

- Supports **first-time mothers**, especially in rural areas
- Helps women with **specific health conditions or dietary restrictions**
- Provides **mental reassurance** through regular, human-like interaction
- Promotes **nutritional awareness** trimester-by-trimester
- Gives timely alerts on symptoms that may require medical attention

---

## ✨ Features

- 🔐 **Secure login system** with hashed passwords (using bcrypt)
- 🆓 **Guest mode** access without signup
- 🤖 GPT-4 powered chatbot trained on a prenatal care knowledge base
- 🧾 **Trimester-based food recommendations** from CSV dataset
- ⚠️ **Symptom-based risk alerts**
- 🎤 **Voice input support** via Google Speech Recognition
- 📁 **Context-aware responses** stored in MongoDB

---

## 🧰 Tech Stack

| Layer        | Technology                          |
|--------------|-------------------------------------|
| Frontend     | Streamlit                           |
| Backend      | Python, OpenAI GPT-4 API            |
| Database     | MongoDB + PyMongo                   |
| Voice Input  | SpeechRecognition (Google API)      |
| Security     | bcrypt, python-dotenv               |

---

## 🚀 Getting Started

Follow these steps to get the application up and running on your local machine.


### 1️⃣ Clone the Repository

git clone https://github.com/your-username/pregnocare-ai.git
cd pregnocare-ai


###2️⃣ Create a Virtual Environment

  python -m venv venv

  
###3️⃣ Activate the Environment
   
  On Windows:
  
    venv\Scripts\activate
  On Mac/Linux:
  
    source venv/bin/activate
###4️⃣ Install Dependencies

  pip install -r requirements.txt


###5️⃣ Set Environment Variables


Create a .env file in the root folder and add:

  OPENAI_API_KEY=your_openai_api_key
  MONGODB_URI=your_mongodb_connection_string


###▶️ Run the App

  streamlit run app.py
  Then open the local URL shown in your terminal (usually http://localhost:8501).

