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

from src.bot.irc_bot import IRCBot

def main():
    bot = IRCBot()
    try:
        bot.start()
    except KeyboardInterrupt:
        print("\nBot shutting down...")
        bot.telegram.send_message("🔴 IRC Bot is shutting down...")
        bot.die()

if __name__ == "__main__":
    main()
