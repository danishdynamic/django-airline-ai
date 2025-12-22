from django.urls import path

from . import views

app_name = 'users'

# now we need functions in views.py: index, login_view, logout_view, register_view

urlpatterns = [
    path(' ', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]

