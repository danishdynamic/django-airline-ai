from rest_framework import serializers
from flights.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ('sentiment_label', 'sentiment_score', 'analyzed_at') # make sentiment fields read-only for api docs 
