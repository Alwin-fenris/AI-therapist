import google.generativeai as genai
system_prompt = "You are a kind, supportive therapist who always gives empathetic and thoughtful advice."

# Set up Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Choose the Gemini model
model = genai.GenerativeModel("gemini-pro")
def get_chatgpt_response(prompt):
    response = model.generate_content(system_prompt + "" + prompt)
    return response.text
