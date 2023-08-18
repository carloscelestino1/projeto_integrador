from django.urls import path
from . import views


urlpatterns = [
    path('', views.teste1, name='teste'),
]
