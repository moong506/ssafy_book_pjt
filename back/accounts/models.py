from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Category, Book

# Create your models here.
class User(AbstractUser):
    # many to many field
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    # foreign key
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # table
    nickname = models.CharField(max_length=20)
    user_id = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20) # 선택할 수 있는 field로?
    age = models.IntegerField()
    weekly_age_reading_time = models.IntegerField()
    annual_reading_amount = models.IntegerField()
    profile_img = models.CharField(max_length=200)



