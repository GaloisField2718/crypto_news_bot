"""
IRC News Bot - A bot that monitors crypto-related news from IRC channels and forwards them to Telegram
Copyright (C) 2024  GaloisField

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import irc.bot
import irc.strings
from src.config import settings
from src.services.telegram import TelegramService
from src.bot.message_handler import MessageHandler
from src.services.news_cache import NewsCache
from src.services.digest_service import DigestService

class IRCBot(irc.bot.SingleServerIRCBot):
    def __init__(self):
        if not settings.TELEGRAM_BOT_TOKEN or not settings.TELEGRAM_CHAT_ID:
            raise ValueError("Please set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env file")
        
        self.telegram = TelegramService(
            settings.TELEGRAM_BOT_TOKEN,
            settings.TELEGRAM_CHAT_ID
        )
        
        irc.bot.SingleServerIRCBot.__init__(
            self,
            [(settings.IRC_SERVER, settings.IRC_PORT)],
            settings.IRC_NICKNAME,
            settings.IRC_NICKNAME
        )
        self.news_cache = NewsCache()
        self.digest_service = DigestService(interval_hours=1)

    def on_welcome(self, connection, event):
        """Called when bot connects to server"""
        connection.join(settings.IRC_CHANNEL)
        print(f"Connected and joined {settings.IRC_CHANNEL}")
        self.telegram.send_message(
            f"🟢 IRC Bot is now connected to {settings.IRC_CHANNEL} channel"
        )

    def on_pubmsg(self, connection, event):
        """Called when a message is received"""
        message = event.arguments[0]
        print(f"Received: {message}")
        
        # Find matching keywords
        matched_keywords = MessageHandler.find_crypto_terms(message)
        
        if matched_keywords:
            if self.news_cache.is_duplicate(message):
                print(f"Skipping duplicate news: {message}")
                return
            
            print(f"Forwarding crypto-related message: {message}")
            self.telegram.send_message(message)
            self.news_cache.add_news(message)
            
            # Add to digest
            self.digest_service.add_news(message, matched_keywords)
    
    def _handle_digest(self, digest_message):
        """Callback for when a digest is generated"""
        self.telegram.send_message(digest_message)
