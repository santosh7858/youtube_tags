from keybert import KeyBERT

kw_model = KeyBERT()

def generate_tags(text, max_keywords=15):
    # Extract keywords using BERT (no manual stopwords or templates!)
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 3), stop_words='english', top_n=max_keywords)

    # Only get the keyword text
    tags = [kw[0] for kw in keywords]

    # Return as comma-separated string
    return ", ".join(tags)
