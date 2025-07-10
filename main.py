import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN, OWNER_ID
from handlers.start import start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    print("Bot started...")
    app.run_polling()