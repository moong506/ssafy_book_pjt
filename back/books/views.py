# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

# from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Book, Book_comment, Thread, Thread_comment, Category # , follower
from .serializers import BookSerializer, BookCommentSerializer, ThreadSerializer, ThreadCommentSerializer

# Create your views here.

# def index(request):
#     pass


# POST요청은 테스트 위해 만든 것! 실제로는 loaddata 이용할듯
@api_view(['GET', 'POST'])
def book_list(request):
    # books = Book.objects.all()
    books = get_list_or_404(Book)
    if request.method == 'GET':
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)


@api_view(['POST'])
def book_picks(request, book_pk):
    pass


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def thread_list(request, book_pk):
    if request.method == 'GET':
        # threads = Thread.objects.all()
        threads = get_list_or_404(Thread)
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        ## test user 생성. postman 사용하기 위함
        # if not request.user.is_authenticated:
        #     User = get_user_model()
        #     user = User.objects.get(username='admin')
        ####

        book = get_object_or_404(Book, pk=book_pk)
        serializer = ThreadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(book=book, user=request.user)

            ## postman 사용 위한 test user 이용 코드. 나중에 삭제할것
            # serializer.save(book=book, user=user)
            ####
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def thread_detail(request, book_pk, thread_pk):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


@api_view(['POST'])
def thread_likes(request, book_pk, thread_pk):
    pass


@api_view(['GET', 'POST'])
def book_comment_list(request, book_pk):
    pass


@api_view(['PUT', 'DELETE'])
def book_comment_update(request, book_pk, book_comment_pk):
    pass


@api_view(['GET', 'POST'])
def thread_comment_list(request, book_pk, thread_pk):
    pass


@api_view(['PUT', 'DELETE'])
def thread_comment_update(request, book_pk, thread_pk, thread_comment_pk):
    pass


