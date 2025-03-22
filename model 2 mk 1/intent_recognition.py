from transformers import pipeline

# Load a zero-shot classification model from Hugging Face
classifier = pipeline("zero-shot-classification")

def classify_intent(text):
    """
    Classify the intent of the user input using a pre-trained model.
    """

    # Define the set of possible intents (labels)
    candidate_labels = ["mood", "advice", "greeting", "stress", "help", "gratitude", "angry", "sad", "happy", "anxiety"]

    # Use the classifier to predict the intent
    result = classifier(text, candidate_labels=candidate_labels)

    # Return the highest probability intent label
    return result['labels'][0]  # The intent with the highest score
from textblob import TextBlob

def get_sentiment(text):
    """
    Analyzes the sentiment of the text and returns a polarity score.
    Sentiment polarity ranges from -1 (negative) to 1 (positive).
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Returns a value between -1 and 1

def adjust_response_based_on_sentiment(response, sentiment):
    """
    Adjusts the AI's response based on sentiment. 
    More empathetic if the sentiment is negative.
    """
    if sentiment < 0:
        response = f"I'm really sorry you're feeling down. {response} Do you want to talk more about it?"
    elif sentiment > 0:
        response = f"That's great to hear! {response} Keep that positive energy going!"
    
    return response
