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
