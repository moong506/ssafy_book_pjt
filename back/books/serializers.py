from rest_framework import serializers
# from .models import Book

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
# class 
