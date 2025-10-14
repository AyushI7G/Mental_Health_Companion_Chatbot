# chat_logic.py

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
from utils import positive_responses, neutral_responses, negative_responses, pick_tip, is_greeting

# Download VADER lexicon at runtime (works in Streamlit Cloud)
nltk.download('vader_lexicon', quiet=True)

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()


def get_sentiment(text):
    """Return 'positive', 'neutral', or 'negative' based on VADER sentiment score."""
    score = sia.polarity_scores(text)["compound"]
    if score >= 0.25:
        return "positive"
    elif score <= -0.25:
        return "negative"
    else:
        return "neutral"


def generate_response(user_input, last_sentiment=None, last_tip=None):
    """
    Generate a chatbot response based on user input.
    Returns: response_text, updated_last_sentiment, updated_last_tip
    """
    text = user_input.lower()

    # --- Greetings ---
    if is_greeting(text):
        return random.choice([
            "Hello! 💚 How are you feeling today?",
            "Hey there! I’m here to listen. How’s your mood?",
            "Hi! 😊 Hope you’re doing well. Want to share how you feel?"
        ]), last_sentiment, last_tip

    # --- Detect sentiment ---
    sentiment = get_sentiment(text)

    # --- Context-aware responses ---
    if sentiment == "negative":
        if last_sentiment == "negative":
            response = random.choice([
                "I hear you. 💛 I know it’s tough, but I’m still here for you.",
                "It’s okay to feel sad again. 🌱 Maybe a small self-care break could help."
            ])
        else:
            response = random.choice(negative_responses)

        # Add new relaxation tip
        tip = pick_tip(last_tip)
        response += " 💡 Tip: " + tip
        last_tip = tip

    elif sentiment == "positive":
        if last_sentiment == "negative":
            response = random.choice([
                "That’s awesome to hear! 🌈 I’m glad things are looking up.",
                "Yay! You turned things around — that’s real strength. 💪"
            ])
        else:
            response = random.choice(positive_responses)

    else:  # neutral
        if last_sentiment == "neutral":
            response = random.choice([
                "I see. Sometimes sitting with your thoughts is totally okay. 🌸",
                "You seem thoughtful — anything specific on your mind?"
            ])
        else:
            response = random.choice(neutral_responses)

    last_sentiment = sentiment
    return response, last_sentiment, last_tip
