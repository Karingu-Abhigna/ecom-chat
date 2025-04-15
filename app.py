"""from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# ✅ Configure Gemini API
genai.configure(api_key="AIzaSyB6IWdtA_E1XjaT3YZxXppENR0A934Vais")  # Use your actual API key

# ✅ Load the correct model
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")  # Make sure model name is correct

# ✅ Define bot response function
def get_bot_response(user_input):
    try:
        prompt = f"Please answer the following with proper Markdown formatting:\n\n{user_input}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# ✅ Set up Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_reply = get_bot_response(user_message)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
"""
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import os

# Load .env first
load_dotenv()

# Debug print (optional)
print("🔍 Pinecone API Key:", os.getenv("PINECONE_API_KEY"))

from chatbot_agent.bot import get_bot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    bot_reply = get_bot_response(user_msg)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
