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
