from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(review):
    scores = analyzer.polarity_scores(review.comment)
    compound = scores["compound"]

    if compound >= 0.05:
        label = "POSITIVE"
    elif compound <= -0.05:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"

    review.sentiment_label = label
    review.sentiment_score = round(abs(compound), 4)
    review.save(update_fields=["sentiment_label", "sentiment_score"])

    #return {    for api endpoint if needed
       # "label": label,
       # "score": round(abs(compound), 4)
    #}
