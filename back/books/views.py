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

def index(request):
    pass

# def recommend_response(request):
#     # 이 안에 utils.py의 ai 코드를 함수로 쓰고..
#     # 그걸 main페이지에서 함수를 호출한 다음에 user=request.user
#     # response로 data를 잘 보내면 된다고..?
#     # return Response(data)
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
        serializer = BookSerializer(book, context={'request':request})
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def book_picks(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    user = request.user

    if book in user.like_books.all():
        user.like_books.remove(book)
        is_picked = False
    else:
        user.like_books.add(book)
        is_picked = True

    return Response({
        'book_id': book.pk,
        'is_picked': is_picked,
        'pick_count': book.like_users.count(),
    })


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def thread_list(request, book_pk):
    if request.method == 'GET':
        # threads = Thread.objects.all()
        # threads = get_list_or_404(Thread)
        threads = Thread.objects.filter(book_id=book_pk)
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
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def thread_detail(request, book_pk, thread_pk):
    book = get_object_or_404(Book, pk=book_pk)
    thread = get_object_or_404(Thread, pk = thread_pk)
    if request.method == 'GET':
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ThreadSerializer(thread, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(book=book, user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def thread_likes(request, book_pk, thread_pk):
    pass


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def book_comment_list(request, book_pk):
    if request.method == 'GET':
        # comments = Book_comment.objects.all()
        comments = get_list_or_404(Book_comment)
        serializer = BookCommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # book = Book.objects.get(pk=book_pk)
        book = get_object_or_404(Book, pk=book_pk)
        serializer = BookCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(book=book, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT', 'DELETE'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def book_comment_detail(request, book_pk, book_comment_pk):
    # book = Book.objects.get(pk=book_pk)
    # comment = Book_comment.objects.get()
    if request.method == 'PUT':
        # book = get_object_or_404(Book, pk=book_pk)
        comment = get_object_or_404(Book_comment, pk=book_comment_pk)
        serializer = BookCommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        comment = get_object_or_404(Book_comment, pk=book_comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def thread_comment_list(request, book_pk, thread_pk):
    if request.method == 'GET':
        comments = Thread_comment.objects.all()
        serializer = ThreadCommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        book = get_object_or_404(Book, pk=book_pk)
        thread = get_object_or_404(Thread, pk=thread_pk)
        serializer = ThreadCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(book=book, thread=thread, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def thread_comment_detail(request, book_pk, thread_pk, thread_comment_pk):
        # book = get_object_or_404(Book, pk=book_pk)
        # thread = get_object_or_404(Thread, pk=thread_pk)
    comment = get_object_or_404(Thread_comment, pk=thread_comment_pk)
    if request.method == 'PUT':
        serializer = ThreadCommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # comment = get_object_or_404(Thread_comment, pk=thread_comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


