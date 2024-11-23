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

from src.config.keywords import CRYPTO_KEYWORDS

class MessageHandler:
    @staticmethod
    def find_crypto_terms(message):
        """
        Check if message contains any crypto-related terms and return matches.
        """
        message_lower = f" {message.lower()} "
        matched_keywords = []
        
        for keyword in CRYPTO_KEYWORDS:
            search_term = f" {keyword} "
            if search_term in message_lower:
                matched_keywords.append(keyword)
                
        return matched_keywords
