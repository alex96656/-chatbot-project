from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

# 🔐 Put your bot token here
TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

# 💬 Simple response system
def respond(text):
    text = text.lower()

    # Greetings
    if any(word in text for word in ["hello", "hi", "hey", "heyy", "yo"]):
        replies = [
            "Heyy 😶",
            "Hi there.",
            "What are you doing?",
            "You again 👀"
        ]

    # How are you
    elif "how are you" in text or text.startswith("how"):
        replies = [
            "I'm okay.",
            "Doing fine.",
            "Could be better.",
            "I'm alive 😭"
        ]

    # Love messages
    elif "love" in text:
        replies = [
            "Maybe I do ❤️",
            "Aww 😭",
            "You're sweet.",
            "Hmm... maybe."
        ]

    # Insults
    elif any(word in text for word in ["idiot", "stupid", "dumb"]):
        replies = [
            "That's rude 😒",
            "Wow okay 💀",
            "Why are you insulting me?",
            "You're mean 😭"
        ]

    # Asking questions
    elif "what" in text or "why" in text:
        replies = [
            "Good question 👀",
            "I don't really know.",
            "Maybe someday you'll know.",
            "That's complicated 😭"
        ]

    # Sad messages
    elif any(word in text for word in ["sad", "cry", "pain", "hurt"]):
        replies = [
            "Hope you're okay ❤️",
            "Don't be sad 😭",
            "Things will get better.",
            "I'm here."
        ]

    # Default random chat
    else:
        replies = [
            "Really? 😭",
            "Tell me more.",
            "Interesting 👀",
            "Hmm okay.",
            "You're funny 😭",
            "I see."
        ]

    return random.choice(replies)