from dj_rest_auth.registration.serializers import RegisterSerializer
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
            'first_name',
            'last_name',
            'profile_img',
            'weekly_avg_reading_time',
            'annual_reading_amount',
            'category',
        )


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField()
    category = serializers.IntegerField(required=False) # required 나중에 true로 바꾸기
    gender = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    weekly_avg_reading_time = serializers.IntegerField(required=False)
    annual_reading_amount = serializers.IntegerField(required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['category'] = self.validated_data.get('category', None)
        data['gender'] = self.validated_data.get('gender', '')
        data['age'] = self.validated_data.get('age', None)
        data['first_name'] = self.validated_data.get('first_name', '')
        data['last_name'] = self.validated_data.get('last_name', '')
        data['weekly_avg_reading_time'] = self.validated_data.get('weekly_avg_reading_time', None)
        data['annual_reading_amount'] = self.validated_data.get('annual_reading_amount', None)
        return data
    
    # def validate_nickname(self, value):
    #     if User.objects.filter(nickname=value).exists():
    #         raise serializers.ValidationError("이미 사용 중인 닉네임입니다.")
    #     return value

    def save(self, request):
        user = super().save(request)
        user.nickname = self.validated_data.get('nickname')
        user.gender = self.validated_data.get('gender')
        user.age = self.validated_data.get('age')
        user.first_name = self.validated_data.get('first_name')
        user.last_name = self.validated_data.get('last_name')
        user.weekly_avg_reading_time = self.validated_data.get('weekly_avg_reading_time')
        user.annual_reading_amount = self.validated_data.get('annual_reading_amount')

        # category: foreign key로, 객체 자체를 할당해야함
        category_id = self.validated_data.get('category')
        if category_id:
            try:
                category = Category.objects.get(pk=category_id)
                user.category = category
            except Category.DoesNotExist:
                pass

        user.save()
        return user



