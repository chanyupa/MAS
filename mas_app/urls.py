from django.urls import path
from mas_app import views



urlpatterns = [
    path('home/',views.home,name="home"),
    path('featuress/',views.featuress,name="featuress"),
    path('pricing/',views.pricing,name="pricing")
]