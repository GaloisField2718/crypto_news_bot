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