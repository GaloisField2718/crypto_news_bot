import openai
from src.config import settings

class AISummaryService:
    def __init__(self):
        if not settings.OPENAI_API_KEY:
            raise ValueError("Please set OPENAI_API_KEY in .env file")
            
        openai.api_key = settings.OPENAI_API_KEY
    
    def generate_summary(self, news_items):
        """Generate an AI summary of multiple news items"""
        try:
            # Combine news items into a single text
            combined_news = "\n".join([item['content'] for item in news_items])
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a crypto news analyst. Summarize the following news items into a brief overview of key developments."},
                    {"role": "user", "content": combined_news}
                ],
                max_tokens=150
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating AI summary: {e}")
            return None 