from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('en/', en_home, name='en_home'),
]
