from celery import shared_task
from django.utils import timezone
from .models import Review
from .services.sentiment import analyze_sentiment

@shared_task
def analyze_review_sentiment(review_id):
    """
    Asynchronous task to analyze sentiment for a review.
    """
    try:
        review = Review.objects.get(id=review_id)
        sentiment = analyze_sentiment(review.comment)
        review.sentiment_label = sentiment["label"]
        review.sentiment_score = sentiment["score"]
        review.analyzed_at = timezone.now()
        review.save()
    except Exception as e:
        print(f"Sentiment analysis failed for review {review_id}: {e}")

@shared_task
def hourly_sentiment_cleanup():
    """
    Cron job: Finds reviews that haven't been analyzed yet 
    (e.g., if the AI service was down) and processes them.
    """
    pending_reviews = Review.objects.filter(sentiment_label__isnull=True)
    
    for review in pending_reviews:
        try:
            sentiment = analyze_sentiment(review.comment)
            review.sentiment_label = sentiment["label"]
            review.sentiment_score = sentiment["score"]
            review.analyzed_at = timezone.now()
            review.save()
        except Exception as e:
            print(f"Cleanup failed for review {review.id}: {e}")