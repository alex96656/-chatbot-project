from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

# 🔐 Put your bot token here
TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

# 💬 Simple response system
def respond(text):
    responses = {
        "hello": ["Hey there 😐", "What do you want?", "Hi... I guess"],
        "how are you": ["I'm fine.", "Stop asking that.", "I'm okay."],
        "i love you": ["Hmm... okay.", "Sure.", "Whatever."],
        "default": ["I don't understand.", "Say something else."]
    }

    text = text.lower()

    if text in responses:
        return random.choice(responses[text])
    else:
        return random.choice(responses["default"])

# 🚀 Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is online.")

# 💬 Chat handler (works in group + private)
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    user_text = update.message.text

    reply = respond(user_text)

    # 👇 Tag user in response
    await update.message.reply_text(f"{user_name}, {reply}")

# ⚙️ Main setup
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Bot is running...")
app.run_polling()
