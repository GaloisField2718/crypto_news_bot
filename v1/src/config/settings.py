from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# IRC Settings
IRC_SERVER = os.getenv('IRC_SERVER', 'irc.libera.chat')
IRC_PORT = int(os.getenv('IRC_PORT', '6667'))
IRC_NICKNAME = os.getenv('IRC_NICKNAME', 'NewsReader')
IRC_CHANNEL = os.getenv('IRC_CHANNEL', '##news')

# Telegram Settings
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Translation Settings
SOURCE_LANG = os.getenv('SOURCE_LANG', 'en')
TARGET_LANG = os.getenv('TARGET_LANG', 'fr')
