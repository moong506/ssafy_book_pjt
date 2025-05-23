from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # path('', views.index, name=''),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_pk>/', views.book_detail, name='book_detail'),


]
