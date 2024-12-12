from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import download

# Ensure necessary NLTK data is downloaded
download('vader_lexicon')

def analyze_sentiment(text):
    """Analyze sentiment of a given text using NLTK's VADER."""
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores  # Returns a dict with 'neg', 'neu', 'pos', and 'compound' scores
