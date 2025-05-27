from django.urls import path
from . import views

# url이 api/v1/임!
app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    # 전체 도서 리스트 조회
    path('books/', views.book_list, name='book_list'),
    # 단일 도서 조회
    path('books/<int:book_pk>/', views.book_detail, name='book_detail'),
    # 도서 찜하기
    path('books/<int:book_pk>/picks/', views.book_picks, name='book_picks'),
    # 특정 도서의 전체 쓰레드 조회 & 쓰레드 생성
    path('books/<int:book_pk>/threads/', views.thread_list, name='thread_list'),
    # 특정 도서의 특정 쓰레드 조회 & 수정 & 삭제
    path('books/<int:book_pk>/threads/<int:thread_pk>/', views.thread_detail, name='thread_detail'),
    # 쓰레드 좋아요
    path('books/<int:book_pk>/threads/<int:thread_pk>/likes/', views.thread_likes, name='thread_likes'),
    # book 댓글 생성 및 전체 댓글 조회 
    path('books/<int:book_pk>/book_comments/', views.book_comment_list, name='book_comment_list'),
    # book 개별 댓글 수정 & 삭제
    path('books/<int:book_pk>/book_comments/<int:book_comment_pk>/', views.book_comment_detail, name='book_comment_detail'),
    # thread 댓글 생성 및 전체 댓글 조회 
    path('books/<int:book_pk>/threads/<int:thread_pk>/thread_comments/', views.thread_comment_list, name='thread_comment_list'),
    # thread 개별 댓글 수정 & 삭제
    path('books/<int:book_pk>/threads/<int:thread_pk>/thread_comments/<int:thread_comment_pk>/', views.thread_comment_detail, name='thread_comment_detail'),
]
