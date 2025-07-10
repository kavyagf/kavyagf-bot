import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
PIN_CODE = os.getenv("PIN_CODE", "000000")
BOT_NAME = os.getenv("BOT_NAME", "Kavya")
NICKNAME = os.getenv("NICKNAME", "Golu")
LANGUAGE = os.getenv("LANGUAGE", "hi")
ENABLE_MEMORY = os.getenv("ENABLE_MEMORY", "false").lower() == "true"
ENABLE_DIRTY_MODE = os.getenv("ENABLE_DIRTY_MODE", "false").lower() == "true"
ENABLE_TANTRA_MODE = os.getenv("ENABLE_TANTRA_MODE", "false").lower() == "true"
MONGODB_URI = os.getenv("MONGODB_URI")