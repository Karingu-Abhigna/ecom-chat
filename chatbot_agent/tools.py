import requests
import os

def get_real_time_info(query):
    headers = {
        'X-API-KEY': os.environ.get("SERPER_API_KEY"),
        'Content-Type': 'application/json'
    }
    response = requests.post("https://google.serper.dev/search", headers=headers, json={"q": query})
    try:
        return response.json()['organic'][0]['snippet']
    except Exception:
        return "Sorry, I couldn't fetch live info right now."
def get_return_policy():
    return "You can return most items within 30 days. Please check product-specific pages."

def get_delivery_eta(location="Nairobi"):
    return f"Delivery to {location} takes 3-5 business days."
