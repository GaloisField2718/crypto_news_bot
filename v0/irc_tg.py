import irc.bot
import irc.strings
import requests
from dotenv import load_dotenv
import os
from keywords import CRYPTO_KEYWORDS

# Load environment variables from .env file
load_dotenv()

class IRCBot(irc.bot.SingleServerIRCBot):
    def __init__(self):
        # Load IRC configuration from .env
        server = os.getenv('IRC_SERVER', 'irc.libera.chat')
        port = int(os.getenv('IRC_PORT', '6667'))
        nickname = os.getenv('IRC_NICKNAME', 'NewsReader')
        
        # Get Telegram credentials from .env
        self.telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
        
        if not self.telegram_token or not self.telegram_chat_id:
            raise ValueError("Please set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env file")
        
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)

    def send_to_telegram(self, message):
        """Send message to Telegram channel"""
        telegram_api_url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        try:
            response = requests.post(
                telegram_api_url,
                json={
                    'chat_id': self.telegram_chat_id,
                    'text': message,
                    'parse_mode': 'HTML'
                }
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error sending message to Telegram: {e}")

    def on_welcome(self, connection, event):
        """Called when bot connects to server"""
        channel = os.getenv('IRC_CHANNEL', '##news')
        connection.join(channel)
        print(f"Connected and joined {channel}")
        # Notify Telegram that IRC bot is online
        self.send_to_telegram(f"🟢 IRC Bot is now connected to {channel} channel")

    def contains_crypto_term(self, message):
        """
        Check if message contains any crypto-related terms.
        Uses word boundary checking to avoid partial matches.
        """
        message_lower = f" {message.lower()} "  # Add spaces for word boundary checking
        
        # Debug: Print the processed message
        print(f"Processing message: {message_lower}")
        
        for keyword in CRYPTO_KEYWORDS:
            # For multi-word keywords, add spaces around the entire phrase
            search_term = f" {keyword} "
            if search_term in message_lower:
                print(f"Matched keyword: {keyword}")
                return True
        return False

    def on_pubmsg(self, connection, event):
        """Called when a message is received"""
        message = event.arguments[0]
        print(f"Received: {message}")  # Log all messages
        
        # Only forward messages containing crypto terms
        if self.contains_crypto_term(message):
            print(f"Forwarding crypto-related message: {message}")
            self.send_to_telegram(message)

if __name__ == "__main__":
    # Create a sample .env file if it doesn't exist
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write("""# IRC Configuration
IRC_SERVER=irc.libera.chat
IRC_PORT=6667
IRC_NICKNAME=YOUR_NICKNAME_HERE
IRC_CHANNEL=YOUR_CHANNEL_HERE

# Telegram Configuration
TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE
TELEGRAM_CHAT_ID=YOUR_CHAT_ID_HERE
""")
        print("Created sample .env file. Please edit it with your credentials.")
        exit(1)

    bot = IRCBot()
    try:
        bot.start()
    except KeyboardInterrupt:
        print("\nBot shutting down...")
        # Notify Telegram that IRC bot is shutting down
        bot.send_to_telegram("🔴 IRC Bot is shutting down...")
        bot.die()



