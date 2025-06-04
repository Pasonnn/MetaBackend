from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookView.as_view(), name='book_view'),
    path('books/<int:pk>/', views.SingleBookView.as_view(), name='single_book_view'),
]
