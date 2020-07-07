from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.basic_app_home, name='basic_app_home'),
    path('travelLists/', views.index, name='travelLists'),  # index
    path('createTrip', views.add_travel, name='createTrip'),  # add new
    path('travelLists/<int:pk>/Details/', views.details, name='details'),
]

