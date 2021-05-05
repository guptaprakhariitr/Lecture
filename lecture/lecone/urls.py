from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name = 'lechome'),
  path('about/', views.about, name = 'lecabout'),
  
]