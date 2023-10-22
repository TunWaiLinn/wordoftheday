# In your Django app's urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/word-details/', views.word_details, name='word-details'),
]
