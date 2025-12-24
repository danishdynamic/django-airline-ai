from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text: str) -> dict:
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"],      # POSITIVE / NEGATIVE
        "score": float(result["score"])
    }
