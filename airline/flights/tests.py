from django.test import TestCase,Client

# Create your tests here.

from django.urls import reverse
from django.contrib.auth.models import User
from .models import Flight, Airport, Passenger, Review

class FlightTestCase(TestCase):

    def setUp(self):

    #1 create a user so we can login
       self.user = User.objects.create_user(username="testuser", password='password')
       self.client = Client()

    #2 create smaple airports ( required for flight foreign keys)

       self.a1 = Airport.objects.create(code="JFK", city="New York")
       self.a2 = Airport.objects.create(code="LHR", city="London")

    def test_create_flight_valid(self):
        """Test that a logged-in user can create a flight"""
        # Log the user in
        self.client.login(username="testuser", password="password")

        # Send a POST request to the 'create' URL
        # Replace 'create_flight' with the actual name in your urls.py
        response = self.client.post(reverse("flights:create_flight"), {
            "origin": self.a1.id,
            "destination": self.a2.id,
            "duration": 400
        })

        # Check if it redirects (status code 302) to the index page
        self.assertEqual(response.status_code, 302)

        # Check if the flight was actually added to the database, assert means verify if true
        self.assertEqual(Flight.objects.count(), 1)
        self.assertEqual(Flight.objects.first().origin.code, "JFK")

    def test_create_flight_logged_out(self):
        """Test that guests are redirected to login if they try to create a flight"""
        response = self.client.post(reverse("flights:create_flight"), {
            "origin": self.a1.id,
            "destination": self.a2.id,
            "duration": 400
        })
        
        # Should redirect to login page (302)
        self.assertEqual(response.status_code, 302)
        # Verify no flight was created
        self.assertEqual(Flight.objects.count(), 0)
    
    
    def test_edit_flight_valid(self):

        # Login first
        self.client.login(username="testuser", password="password")
        # Create a flight to edit
        flight = Flight.objects.create(origin=self.a1,
                                        destination=self.a2, duration=300)

        # Send a POST request to edit the flight
        response = self.client.post(reverse("flights:edit_flight", args=(flight.id,)),{
            "origin" : self.a1.id,
            "destination" : self.a2.id,
            "duration" : 400
        })
        # Should redirect
        self.assertEqual(response.status_code, 302)
        # Verify the flight was updated
        self.assertEqual(Flight.objects.count(), 1)
        # Verify the duration was updated
        flight.refresh_from_db()
        self.assertEqual(flight.duration, 400)


    def test_delete_flight_valid(self):
        # Login first
        self.client.login(username="testuser", password="password")
        # Create a flight to delete
        flight = Flight.objects.create(origin=self.a1,
                                        destination=self.a2, duration=300)
        # Send a POST request to delete the flight
        response = self.client.post(reverse("flights:delete_flight", args=(flight.id,)))
        # Should redirect
        self.assertEqual(response.status_code, 302)
        # Verify the flight was deleted
        self.assertEqual(Flight.objects.count(), 0)


    def test_book_flight(self):
        # Create a flight and a passenger
        flight = Flight.objects.create(origin=self.a1,
                                        destination=self.a2, duration=300)
        passenger = Passenger.objects.create(name="John Doe")

        # Send a POST request to book the flight for the passenger
        response = self.client.post(reverse("flights:book", args=(flight.id,)), {
            "passenger": passenger.id
        })

        # Should redirect
        self.assertEqual(response.status_code, 302)

        # Verify the passenger is booked on the flight
        self.assertIn(flight, passenger.flights.all())




    def test_add_review(self):
       #login user first
        self.client.login(username="testuser", passowrd="password")

        # Create a flight
        flight = Flight.objects.create(origin=self.a1,
                                        destination=self.a2, duration=300)

        # Send a POST request to add a review
        response = self.client.post(reverse("flights:add_review"), {
            "flight": flight.id,
            "name": "John Doe",
            "rating": 5,
            "comment": "Great flight!"
        })

        # Should redirect
        self.assertEqual(response.status_code, 302)

        # Verify the review was added
        self.assertEqual(Review.objects.count(), 1) # 1 means one review added
        review = Review.objects.first()
        self.assertEqual(review.flight, flight)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Great flight!")