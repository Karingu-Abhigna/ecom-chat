import os
import google.generativeai as genai
from .memory import get_memory
from .tools import get_real_time_info
from .tools import get_return_policy, get_delivery_eta
# Load Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro")

memory = get_memory()

from .tools import get_return_policy, get_delivery_eta

def get_bot_response(user_input):
    try:
        prompt = f"You are a helpful e-commerce support assistant.\nUser asked: {user_input}"

        # Check if the user is asking for specific info
        if "return policy" in user_input.lower():
            return get_return_policy()
        elif "delivery" in user_input.lower():
            return get_delivery_eta()

        # Generate response if it's not a specific request
        response = model.generate_content(prompt)
        reply = response.text.strip()

        # Save input-output context to memory
        memory.save_context({"input": user_input}, {"output": reply})

        return reply if reply else get_real_time_info(user_input)

    except Exception as e:
        print(f"⚠️ Gemini error: {e}")
        return get_real_time_info(user_input)
