from datetime import datetime, timedelta
from collections import Counter
import threading
import time

class DigestService:
    def __init__(self, interval_hours=6):
        self.interval_hours = interval_hours
        self.news_items = []
        self.keywords_counter = Counter()
        self.last_digest_time = datetime.now()
        
        # Start the digest timer
        self.timer_thread = threading.Thread(target=self._digest_timer, daemon=True)
        self.timer_thread.start()
    
    def add_news(self, news, keywords):
        """Add a news item and its triggering keywords to the digest"""
        self.news_items.append({
            'timestamp': datetime.now(),
            'content': news,
            'keywords': keywords
        })
        # Update keywords counter
        self.keywords_counter.update(keywords)
    
    def generate_digest(self):
        """Generate a digest of news from the last interval"""
        now = datetime.now()
        
        # Get top keywords
        top_keywords = [kw for kw, _ in self.keywords_counter.most_common(3)]
        while len(top_keywords) < 3:
            top_keywords.append("N/A")
            
        # Format news list
        news_list = "\n".join([
            f"• {item['content']}" 
            for item in self.news_items
        ])
        
        digest_message = (
            f"📰 Crypto News Digest\n\n"
            f"Between {self.last_digest_time.strftime('%Y-%m-%d %H:%M')} and "
            f"{now.strftime('%Y-%m-%d %H:%M')}, "
            f"there were {len(self.news_items)} news items.\n\n"
            f"Top keywords: #{top_keywords[0]}, #{top_keywords[1]}, #{top_keywords[2]}\n\n"
            f"News list:\n{news_list}"
        )
        
        # Reset counters
        self.news_items = []
        self.keywords_counter.clear()
        self.last_digest_time = now
        
        return digest_message
    
    def _digest_timer(self):
        """Timer thread that triggers digest generation"""
        while True:
            time.sleep(self.interval_hours * 3600)  # Convert hours to seconds
            if self.news_items:  # Only generate digest if there are news
                yield self.generate_digest() 