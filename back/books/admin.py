from django.contrib import admin
from .models import Category, Book, Thread, Book_comment, Thread_comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Thread)
admin.site.register(Book_comment)
admin.site.register(Thread_comment)




