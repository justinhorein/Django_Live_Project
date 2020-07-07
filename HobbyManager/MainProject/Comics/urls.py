from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.comics_home, name='comics_home'),
    path('Collection/', views.index, name='listComics'),  # index of comics
    path('AddToCollection/', views.add_book, name='createBook'),  # add new book to collection
    path('Collection/<int:pk>/Details/', views.details_book, name='bookDetails'),  # get details for a single book
    path('Collection/<int:pk>/Edit/', views.post_edit, name='post_edit'),  # edit a single book
    path('Collection/<int:pk>/ConfirmDelete/', views.book_delete, name='book_delete'),
]
