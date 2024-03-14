import spacy
from collections import Counter

# Load English model
nlp = spacy.load("en_core_web_sm")

def analyze_text(response_text):
    # Tokenization
    doc = nlp(response_text)
    tokens = [token.text for token in doc]

    # Named Entity Recognition (NER)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Sentiment Analysis
    sentiment = doc.sentiment

    return tokens, entities, sentiment

# Example usage
response_text = "Sample survey response text"
tokens, entities, sentiment = analyze_text(response_text)
print("Tokens:", tokens)
print("Entities:", entities)
print("Sentiment:", sentiment)
