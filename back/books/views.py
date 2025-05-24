# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404, get_list_or_404

# from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Book, Book_comment, Thread, Thread_comment, Category # , follower
from .serializers import BookSerializer, BookCommentSerializer, ThreadSerializer, ThreadCommentSerializer

# Create your views here.

# def index(request):
#     pass


# POST요청은 테스트 위해 만든 것! 실제로는 loaddata 이용할듯
@api_view(['GET', 'POST'])
def book_list(request):
    books = Book.objects.all()
    if request.method == 'GET':
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def book_detail(request, book_pk):
    book = get_object_or_404(Book, book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(data=request.data)
        return Response(serializer.data)






