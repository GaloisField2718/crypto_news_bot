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

from datetime import datetime, timedelta

class NewsCache:
    def __init__(self, expiration_hours=24):
        self.cache = {}
        self.expiration_hours = expiration_hours

    def add_news(self, title):
        """Add a news title to cache with current timestamp"""
        clean_title = self._clean_title(title)
        self.cache[clean_title] = datetime.now()
        self._cleanup_expired()

    def is_duplicate(self, title):
        """Check if news title already exists in cache"""
        clean_title = self._clean_title(title)
        self._cleanup_expired()
        return clean_title in self.cache

    def _clean_title(self, title):
        """Extract and clean the actual title from the news format"""
        try:
            # Remove source prefix and URL
            title_part = title.split('] ')[1].split(' → ')[0]
            return title_part.lower().strip()
        except IndexError:
            return title.lower().strip()

    def _cleanup_expired(self):
        """Remove entries older than expiration_hours"""
        current_time = datetime.now()
        expired_titles = [
            title for title, timestamp in self.cache.items()
            if current_time - timestamp > timedelta(hours=self.expiration_hours)
        ]
        for title in expired_titles:
            del self.cache[title] 