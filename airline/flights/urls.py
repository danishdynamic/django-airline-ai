from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
   
   path("", views.index, name="index"),
   path("create/", views.create_flight, name="create_flight"),
   path("edit/<int:flight_id>/", views.edit_flight, name="edit_flight"),
   path("delete/<int:flight_id>/", views.delete_flight, name="delete_flight"),
   path('flights/review/', views.add_review, name= 'add_review'),
   path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
   path('book/<int:flight_id>/', views.book, name='book'),
]