import spacy
from collections import Counter

# Load English language model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text: str, top_n: int = 3):
    doc = nlp(text)
    nouns = [token.lemma_.lower() for token in doc if token.pos_ == "NOUN"]
    common = Counter(nouns).most_common(top_n)
    return [word for word, _ in common]
