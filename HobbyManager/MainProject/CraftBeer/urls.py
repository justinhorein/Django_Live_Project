from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='craftbeer'), #home page
    path('Collection/', views.index, name='listBeers'), # collection page
    path('AddToCollection/', views.add_beer, name='createBeer'),  # add new beer
    path('Collection/<int:pk>/Details/', views.details_beer, name='beerDetails'), # get details for a single beer
    path('Collection/<int:pk>/Edit/', views.edit_beer, name='editBeer'), # edit details for a beer
    path('Collection/<int:pk>/Delete/', views.delete_beer, name='deleteBeer'), # delete beer
]