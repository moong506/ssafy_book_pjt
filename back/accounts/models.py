from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Category, Book

# Create your models here.
class User(AbstractUser):
    # many to many field
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    # foreign key
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    like_books = models.ManyToManyField(Book, related_name='like_users', blank=True)

    # table
    nickname = models.CharField(max_length=20) #, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True) #
    last_name = models.CharField(max_length=100, null=True, blank=True) # 
    email = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', '남성'),
        ('F', '여성'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) # 선택할 수 있는 field로?
    age = models.PositiveIntegerField() #positive integer로 변경
    weekly_avg_reading_time = models.PositiveIntegerField(null=True, blank=True) #
    annual_reading_amount = models.PositiveIntegerField(null=True, blank=True) #
    profile_img = models.ImageField(max_length=200, null=True, blank=True)



