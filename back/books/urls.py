from django.urls import path
from . import views

# url이 api/v1/임!
app_name = 'books'

urlpatterns = [
    # path('', views.index, name=''),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_pk>/', views.book_detail, name='book_detail'),
    path('books/<int:book_pk>/picks/', views.book_picks, name='book_picks'),
    path('books/<int:book_pk>/threads/', views.thread_list, name='thread_list'),
    path('books/<int:book_pk>/threads/<int:thread_pk>/', views.thread_detail, name='thread_detail'),
    path('books/<int:book_pk>/threads/<int:thread_pk>/likes/', views.thread_likes, name='thread_likes'),
    path('books/<int:book_pk>/book_comments/', views.book_comment_list, name='book_comment_list'),
    path('books/<int:book_pk>/comments/<int:book_comment_pk>/', views.book_comment_update, name='book_comment_update'),
    path('books/<int:book_pk>/threads/<int:thread_pk>/thread_comments/', views.thread_comment_list, name='thread_comment_list'),
    path('books/<int:book_pk>/threads/<int:thread_pk>/thread_comments/<int:thread_comment_pk>', views.thread_comment_update, name='thread_comment_update'),
]
