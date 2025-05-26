from rest_framework import serializers
from .models import Book, Book_comment, Thread, Thread_comment, Category #, follower
from accounts.serializers import UserSerializer

# 참고용, drf with vue 2의 serializers.py

# class ArticleListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ('id', 'title', 'content') # 이렇게 user를 제외해도 되겠지만


# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         read_only_fields = ('user',) # 볼 때 이 정보가 있으면 더 좋겠죠?
#         # 그런데 이걸 쓰기는 싫고, 읽고만 싶어서 read_only_fields를 이용

# books/serializers.py
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # read_only_fields = ('category',)


class BookCommentSerializer(serializers.ModelSerializer):
    class BookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('title',)

    user = UserSerializer(read_only=True)

    class Meta:
        model = Book_comment
        fields = '__all__'
        read_only_fields = ('user', 'book', 'created_at', 'updated_at',)


class ThreadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # user 필드를 UserSerializer로 직렬화
    class Meta:
        model = Thread
        fields = '__all__'
        read_only_fields = ('user', 'book', 'created_at', 'updated_at',)

# book/thread detail serializer 추가하기

class ThreadCommentSerializer(serializers.ModelSerializer):
    class BookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('title',)

    class ThreadSerializer(serializers.ModelSerializer):
        class Meta:
            model = Thread
            fields = ('title',)

    user = UserSerializer(read_only=True)

    class Meta:
        model = Thread_comment
        fields = '__all__'
        read_only_fields = ('user', 'book', 'thread', 'created_at', 'updated_at',)



