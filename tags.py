import re
from itertools import combinations

def generate_tags(text, max_phrases=10):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)

    stopwords = set([
        'the', 'is', 'in', 'for', 'and', 'of', 'to', 'a', 'on', 'with', 'by',
        'from', 'at', 'this', 'that', 'these', 'those', 'it', 'an'
    ])

    words = [word for word in text.split() if word not in stopwords]
    phrases = list(set([
        " ".join(p) for p in combinations(words, 2)
    ]))

    return ", ".join(phrases[:max_phrases])
