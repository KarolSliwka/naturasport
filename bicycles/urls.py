from django.urls import path
from . import views

urlpatterns = [
    path('', views.bicycles, name='bicycles'),
]
