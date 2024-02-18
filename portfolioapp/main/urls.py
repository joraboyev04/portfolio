from django.urls import path
from main.views import *

urlpatterns = [
   path('', Home, name='home'),
   path('send-msg/', SendMsg),
]