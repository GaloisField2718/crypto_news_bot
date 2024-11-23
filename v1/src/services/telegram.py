import requests

class TelegramService:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{token}/sendMessage"

    def send_message(self, message):
        """Send message to Telegram channel"""
        try:
            response = requests.post(
                self.api_url,
                json={
                    'chat_id': self.chat_id,
                    'text': message,
                    'parse_mode': 'HTML'
                }
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error sending message to Telegram: {e}")
