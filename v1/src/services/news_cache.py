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