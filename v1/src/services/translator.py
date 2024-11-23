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

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class TranslatorService:
    def __init__(self, source_lang="en", target_lang="fr"):
        self.model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
        
        # Load model and tokenizer
        print(f"Loading translation model: {self.model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        
        # Move model to GPU if available
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = self.model.to(self.device)
        print(f"Translation model loaded and running on {self.device}")

    def translate(self, text):
        """Translate the given text"""
        try:
            # Tokenize the text
            inputs = self.tokenizer(text, return_tensors="pt", padding=True)
            inputs = inputs.to(self.device)

            # Generate translation
            outputs = self.model.generate(**inputs, max_length=512)
            
            # Decode the translation
            translation = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return translation
        except Exception as e:
            print(f"Translation error: {e}")
            return text  # Return original text if translation fails 