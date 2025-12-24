from rest_framework.viewsets import ModelViewSet
from flights.models import Review
from .serializers import ReviewSerializer
from flights.services.sentiment import analyze_sentiment
from django.utils import timezone
from drf_spectacular.utils import extend_schema, OpenApiParameter


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # Move the decorator here so Swagger picks it up
    @extend_schema(
        summary="Create a new review",
        description="Create a new flight review and perform AI-generated sentiment analysis.",
        responses={201: ReviewSerializer},
    )
    
    def create(self, request, *args, **kwargs):    # override create to add sentiment analysis logic for reviews documentation
        return super().create(request, *args, **kwargs)
    
    @extend_schema(
        summary="List all reviews",
        description="Retrieve a list of all flight reviews including AI-generated sentiment scores."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        # 1. Save the initial review to get an ID  
        review = serializer.save()

        # 2. Add error handling for the AI service
        try:
            sentiment = analyze_sentiment(review.comment)
            review.sentiment_label = sentiment["label"]
            review.sentiment_score = sentiment["score"]
            review.analyzed_at = timezone.now()
            # 3. Save the updated fields
            review.save()
        except Exception as e:
            # If the LLM service is down, we still want the review saved
            # but maybe we log the error or set a "pending" status
            print(f"Sentiment Analysis failed: {e}")
