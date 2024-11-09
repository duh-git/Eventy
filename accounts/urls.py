from django.urls import path
from .views import *


urlpatterns = [
    path('', entrance, name='entrance'),
    path('registration', registration, name='registration'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
]