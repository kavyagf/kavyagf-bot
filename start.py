from telegram import Update
from telegram.ext import ContextTypes
from config import NICKNAME, BOT_NAME

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Hey {NICKNAME} 💋\nI'm {BOT_NAME} — ready to please, teach, and remember everything just for you ❤️"
    )