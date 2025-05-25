from rest_framework import serializers
from .models import User
from books.models import Book, Category

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'nickname',
            'email',
            'gender',
            'age',
            'profile_img',
            'weekly_age_reading_time',
            'annual_reading_amount',
            'category',
        )



