from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Flight, Review, Passenger
from .forms import FlightForm, ReviewForm
from django.contrib.auth.decorators import login_required

from flights.services.sentiment import analyze_sentiment

# Create your views here.
# GET (get the data), POST (sends data ), PUT (update the data), and DELETE

#def index(request):hh
   #return render( request, "flights/index.html",
       # {"flights": Flight.objects.all()}  )

def index(request):
    flights = Flight.objects.all()
    #reviews = Review.objects.select_related('flight').all()
    reviews = Review.objects.all()
    all_passengers = Passenger.objects.all()

    return render(request, 'flights/index.html', {
        'flights': flights,
        'reviews': reviews,
        'all_passengers': all_passengers,
    })

@login_required
def create_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()          
            messages.success(request, 'Flight created successfully!')
            return redirect('flights:index')
    else:
        form = FlightForm()
    return render(request, 'flights/create_flight.html', {'form': form})

def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)  
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flight updated successfully!')
            return redirect('flights:index')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'flights/edit_flight.html', {'form': form, 'flight': flight})

def delete_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        flight.delete()
        messages.success(request, 'Flight deleted successfully!')
        return redirect('flights:index')
    return render(request, 'flights/delete_flight.html', {'flight': flight})

def book(request, flight_id):
    if request.method == 'POST':
        # Get the speicifc flight
        flight = Flight.objects.get(pk=flight_id)
        # get passsenger id from deropdown menu 
        passenger_id= int(request.POST['passenger'])
        passenger = Passenger.objects.get(pk=passenger_id)
        # add flight to passengers flight
        passenger.flights.add(flight)

        return redirect('flights:index')

def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review =form.save()        # Save the form in review variable
            analyze_sentiment(review)  # Call sentiment analysis function
            return redirect('flights:index')
        else:
            print("FORM ERRORS",form.errors)  # DEBUG: shows why it fails
    else:
        form = ReviewForm()

    return render ( request, 'flights/add_review.html', {'form' : form} )   



def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('flights:index')