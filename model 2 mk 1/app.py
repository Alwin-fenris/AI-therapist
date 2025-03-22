from flask import Flask, render_template, request
from chatgpt_integration import get_chatgpt_response  # Import the ChatGPT function
from intent_recognition import classify_intent  # Import the intent classifier
import pandas as pd
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']

    # Step 1: Classify the intent of the user input
    intent = classify_intent(user_input)

    # Step 2: Generate a response based on the classified intent
    if intent == "mood":
        prompt = f"The user is talking about their mood: {user_input}. Provide a supportive response."
    elif intent == "advice":
        prompt = f"The user is asking for advice: {user_input}. Offer some guidance."
    elif intent == "greeting":
        prompt = f"User greeted you with: {user_input}. Respond warmly."
    elif intent == "stress":
        prompt = f"The user is expressing stress: {user_input}. Offer stress-relief advice."
    elif intent == "help":
        prompt = f"The user is asking for help: {user_input}. Offer assistance."
    elif intent == "gratitude":
        prompt = f"The user is expressing gratitude: {user_input}. Respond with appreciation."
    elif intent == "angry":
        prompt = f"The user is expressing anger: {user_input}. Respond with empathy."
    elif intent == "sad":
        prompt = f"The user is feeling sad: {user_input}. Offer emotional support."
    elif intent == "happy":
        prompt = f"The user is feeling happy: {user_input}. Respond with enthusiasm."
    elif intent == "anxiety":
        prompt = f"The user is talking about anxiety: {user_input}. Provide calming advice."
    else:
        prompt = f"The user said: {user_input}. Respond appropriately."

    # Get a response from ChatGPT based on the prompt
    response = get_chatgpt_response(prompt)

    return render_template('index.html', user_input=user_input, response=response)
import pandas as pd

# Create an empty DataFrame to store user input and AI responses
session_data = pd.DataFrame(columns=["user_input", "intent", "ai_response"])

def save_session(user_input, intent, ai_response):
    """
    Save each therapy session into a pandas DataFrame.
    """
    new_session = {"user_input": user_input, "intent": intent, "ai_response": ai_response}
    global session_data
    session_data = session_data.append(new_session, ignore_index=True)
    # Optionally, save it to a CSV to keep a history
    session_data.to_csv("therapy_sessions.csv", index=False)

if __name__ == '__main__':
    app.run(debug=True)
