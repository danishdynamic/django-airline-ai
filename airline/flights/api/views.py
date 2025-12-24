from rest_framework.viewsets import ModelViewSet
from flights.models import Review
from .serializers import ReviewSerializer
from flights.services.sentiment import analyze_sentiment
from django.utils import timezone

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        review = serializer.save()

        sentiment = analyze_sentiment(review.comment)

        review.sentiment_label = sentiment["label"]
        review.sentiment_score = sentiment["score"]
        review.analyzed_at = timezone.now()
        review.save()
