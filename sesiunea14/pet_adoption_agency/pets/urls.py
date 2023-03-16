from django.urls import path
from . import views
app_name = 'pets'

# VERSION 01 - for functions
"""
urlpatterns = [
    path('', views.pets, name='all_pets'),
    path('<int:pet_id>/', views.pet_details, name='pet_details'),
    path('pet/', views.pet_add, name='add')
]
"""


# VERSION 02 - IMPROVED
urlpatterns = [
    path('', views.PetsView.as_view(), name='all_pets'),
    path('<int:pk>/', views.PetDetailView.as_view(), name='pet_details'),
    path('pet/', views.PetCreate.as_view(), name='add')
]
