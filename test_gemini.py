import google.generativeai as genai

# Use your real API key here
genai.configure(api_key="AIzaSyB6IWdtA_E1XjaT3YZxXppENR0A934Vais")

# Use a valid model name from your list
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

# Create prompt
prompt = "Tell me a joke about pineapples"

# Generate response
response = model.generate_content(prompt)

# Output response
print("Response:", response.text)
models = genai.list_models()
for m in models:
    print(m.name)

