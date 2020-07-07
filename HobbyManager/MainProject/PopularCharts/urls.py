from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='charts_home'),
    path('addsongs/', views.add_song, name='song_add' ),
    path('index/', views.index, name='song_index'),
    path('index/<int:pk>/details/', views.details_song, name='songDetails'),  # get details for a single book

]