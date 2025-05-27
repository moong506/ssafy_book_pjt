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

from openai import OpenAI
from django.conf import settings
import json

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):

    user = request.user
    books = user.like_books.all()

    prompt = f"""
    나는 {user.age}세 {user.gender}이고, 주간 독서량은 {user.weekly_avg_reading_time}시간이야.
    내가 최근에 재미있게 읽은 책은 다음과 같아:
    {', '.join(book.title for book in books)}

    이 정보를 바탕으로 나에게 어울리는 책을 5권만 JSON 배열 형태로 추천해줘. 
    형식은 반드시 아래처럼 맞춰줘:

    [
      {{
        "book": "책 제목",
        "author": "작가 이름",
        "content": "간단한 책 설명"
      }},
      ...
    ]

    JSON 외에 다른 말은 절대 하지 말고, 결과만 배열 형태로 반환해줘.
    """

    try:
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        content = response.choices[0].message.content

        try:
            recommendations = json.loads(content)
        except json.JSONDecodeError:
            return Response({"error": "GPT 응답을 JSON으로 파싱할 수 없습니다.", "raw": content}, status=500)

        return Response({"recommendations": recommendations})

    except Exception as e:
        print("OpenAI 호출 중 오류 발생:", e)
        return Response({"error": str(e)}, status=500)
    # user = request.user
    # books = user.like_books.all()

    # prompt = f"""
    # 나는 {user.age}세 {user.gender}이고, 주간 독서량은 {user.weekly_avg_reading_time}시간이야.
    # 내가 최근에 재미있게 읽은 책은 다음과 같아:
    # {', '.join(book.title for book in books)}
    # 이 정보를 바탕으로 나에게 어울리는 책을 무조건 5권 추천해줘. 각 책에 간단한 설명도 부탁해.
    # """

    # try:
    #     client = OpenAI(api_key=settings.OPENAI_API_KEY)
    #     response = client.chat.completions.create(
    #         model="gpt-4o-mini",
    #         messages=[
    #             {"role": "user", "content": prompt}
    #         ]
    #     )
    #     response_text = response.choices[0].message.content
    #     return Response({"recommendations": response_text})

    # except Exception as e:
    #     print("OpenAI 호출 중 오류 발생:", e)
    #     return Response({"error": str(e)}, status=500)
    # return Response({'message': 'OK'})

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
    print(request.user)

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


