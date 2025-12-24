from django.db import models

# Create your models here. which means create data here 
# models → admin - form → view → template → URL

class Airport(models.Model):
   code = models.CharField(max_length=3)
   city = models.CharField(max_length=64)

   def __str__(self):
      return f"{self.city} ({self.code}) "

class Flight(models.Model):
    #origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    #destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
      return f"{self.id } : {self.origin} to {self.destination}"
    
    

# we can add review model here 


class Review(models.Model):
   flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="reviews")
   name = models.CharField(max_length=50)
   rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
   comment = models.TextField()
   created = models.DateTimeField(auto_now_add=True)
  
   #adding sentiment fields
   sentiment_label = models.CharField(max_length=20, null=True, blank=True)
   sentiment_score = models.FloatField(null=True, blank=True)

   analyzed_at = models.DateTimeField(null=True, blank=True)

   def __str__(self):
      return f"Review for {self.flight} by {self.name}"
   
# many tomany relationship

class Passenger(models.Model):
   name = models.CharField(max_length=64)
   flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

   def __str__(self):
      return self.name