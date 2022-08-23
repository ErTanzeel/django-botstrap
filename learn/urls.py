from django.urls import path
from . import views

urlpatterns = [
    path('Home', views.Home, name='Home'),

    path('', views.login, name='login'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path('signout', views.signout, name='signout'),
    path('pay', views.pay, name='pay'),



]
