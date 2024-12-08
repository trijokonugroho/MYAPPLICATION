from django.urls import path

from . import views

urlpatterns = [
    path("books/", views.BookList.as_view(), name= "books"),
    path("books/<int:Book_id>/", views.BookList.as_view(), name= "book"),
    path("books/create/", views.BookList.as_view(), name= "create_book"),
    path("books/update/<int:Book_id>/", views.BookList.as_view(), name= "update_book"),
    path("books/delete/<int:Book_id>/", views.BookList.as_view(), name= "delete_book"),
]