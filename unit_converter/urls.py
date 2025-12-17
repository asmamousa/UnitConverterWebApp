from django.urls import path
from .views import length_converter, weight_converter, temperature_converter

urlpatterns = [
    path('', length_converter, name='length'),
    path('weight/', weight_converter, name='weight'),
    path('temperature/', temperature_converter, name='temperature'),

]