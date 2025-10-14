import random

# --- Relaxation tips ---
relaxation_tips = [
    "Try a 5-minute meditation. 🧘",
    "Take a short walk outside and breathe deeply. 🌳",
    "Listen to your favorite music. 🎵",
    "Write down 3 things you're grateful for today. ✍️",
    "Drink some water and stretch for a minute. 💧",
    "Close your eyes and take 3 deep breaths. 🌬️"
]

# --- Responses ---
positive_responses = [
    "That's wonderful! 🌟 Keep spreading those positive vibes!",
    "Awesome! Remember, your happiness is contagious! 😄",
    "Yay! It’s great to see you feeling good today. 🎉",
    "Love that energy! Keep it up! 💪"
]

neutral_responses = [
    "Thanks for sharing. 🤗 It’s completely okay to have mixed feelings.",
    "I hear you. 🌱 Life has ups and downs, and that’s okay.",
    "It’s normal to feel this way sometimes. Take it one step at a time. 💛",
    "I understand. Want to tell me a bit more about what’s on your mind?"
]

negative_responses = [
    "I’m here for you. 💛 Tough times pass, and you’re stronger than you think.",
    "It’s okay to feel down. You’re not alone in this journey. 🌿",
    "That sounds tough, but I believe in you. 💚",
    "It’s okay to not be okay sometimes. Take a deep breath with me. 🌬️"
]

# --- Helper functions ---
def is_greeting(text):
    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
    return any(word in text.lower() for word in greetings)

def pick_tip(last_tip):
    tips = [t for t in relaxation_tips if t != last_tip]
    tip = random.choice(tips)
    return tip
