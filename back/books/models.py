from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    # foreign key
    # category? category_pk?
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    # table
    title = models.CharField(max_length=100)
    description = models.TextField()
    isbn = models.CharField(max_length=50)
    cover_img = models.CharField(max_length=200) # cover img 지정할 링크
    publisher = models.CharField(max_length=100)
    pub_date = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    author_info = models.TextField(max_length=200)
    # category = models.IntegerField()

    is_bestseller = models.CharField(max_length=10, default='N') # bestseller의 경우 y, default는 n


class Book_comment(models.Model):
    # foreign key
    # user_pk, book_pk
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # table
    comment_description = models.CharField(max_length=200)
    comment_created_at = models.DateTimeField(auto_now_add=True)
    comment_updated_at = models.DateTimeField(auto_now=True)


class Thread(models.Model):
    # foreign key
    # user_pk, book_pk
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # table
    title = models.CharField(max_length=100)
    description = models.TextField()
    read_date = models.DateField()
    cover_img = models.CharField(max_length=200)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Thread_comment(models.Model):
    # foreign key
    # user_pk, thread_pk
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # table
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# accounts/models.py의 User class에서 followings로?
# class follower(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)




