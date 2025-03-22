from transformers import pipeline
import torch
import json
from flask import Flask, render_template, request
from flask_socketio import SocketIO

# Load the intent recognition model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# AI memory (loads from a file)
def load_memory():
    try:
        with open("memory.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"conversations": []}

def save_memory(memory):
    with open("memory.json", "w") as file:
        json.dump(memory, file, indent=4)

memory = load_memory()

# Flask app for the web UI
app = Flask(__name__)
socketio = SocketIO(app)

# Categories for intent recognition
intents = ["emotional support", "advice", "casual talk", "self-improvement", "mental health"]

# Function to generate AI response
def generate_response(user_input):
    classification = classifier(user_input, intents)
    detected_intent = classification["labels"][0]  # Most likely intent

    # Simple response logic (improves over time)
    if detected_intent == "emotional support":
        response = "I'm here for you. Tell me more about how you're feeling."
    elif detected_intent == "advice":
        response = "That sounds important. What kind of advice do you need?"
    elif detected_intent == "casual talk":
        response = "That’s interesting! Tell me more about that."
    elif detected_intent == "self-improvement":
        response = "Self-growth is great! What areas do you want to improve?"
    elif detected_intent == "mental health":
        response = "Mental health is important. Do you want to talk about what’s on your mind?"
    else:
        response = "I'm here to listen. Tell me more."

    # Store in memory
    memory["conversations"].append({"user": user_input, "intent": detected_intent, "response": response})
    save_memory(memory)

    return response

# WebSocket connection
@socketio.on("message")
def handle_message(message):
    response = generate_response(message)
    socketio.send(response)

# Web UI
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)
