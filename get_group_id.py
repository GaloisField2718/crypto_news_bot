import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN')

# Set up logging to capture messages and actions
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle messages and log the group ID
async def get_group_id(update: Update, context: CallbackContext):
    # Get the chat ID (group ID)
    chat_id = update.effective_chat.id
    logger.info(f"Group ID: {chat_id}")
    # Optionally, send the group ID back to the group to confirm
    await update.message.reply_text(f"The group ID is: {chat_id}")

# Set up the application with your bot token
app = Application.builder().token(TELEGRAM_TOKEN).build()

# Add the message handler for any text message
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_group_id))

# Start the bot
app.run_polling()

