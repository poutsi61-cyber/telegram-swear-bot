from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import Update
import asyncio

# ⚠️ Your BotFather token
TOKEN = "8568514179:AAGWz9A9nc8cRVRqh3bheQUou_s-Q_EC_gQ"

# List of Myanmar swear words
bad_words = [
    "မင်းမေစက်ပတ်",
    "ငါလိုး",
    "ငါလိုးမသား",
    "မအေလိုး",
    "လီးပဲ",
    "စပ",
    "စက်ပတ်",
    "စတ်ပတ်",
    "စတ်ပက်",
    "စက်ပက်",
    "လီးပဲ",
    "ငါလိုးလိုပဲ",
    "လီးလိုပဲကွာ",
    "မင်းမေလိုးလား",
    "မင်းမေလိုးလိုက်",
    "လီးစား",
    "စပစား",
    "စတ်ပတ်စား",
    "စောက်ပတ်",
    "စောက်ပတ်ပဲ",
    "ကိုမေကိုလိုး",
    "မင်းမေလိုး"
]

# Function to check for bad words
async def check_swear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    for word in bad_words:
        if word in text:
            await update.message.reply_text(
                "⚠️ ကျေးဇူးပြု၍ ဆဲရေးခြင်း မလုပ်ပါနှင့်။ Group ထဲမှာ ယဉ်ကျေးစွာ ပြောပါ။"
            )

# Build the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add handler for all text messages
app.add_handler(MessageHandler(filters.TEXT, check_swear))

# Start the bot
app.run_polling()
