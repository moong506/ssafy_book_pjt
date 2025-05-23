# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404, get_list_or_404

# from .serializers import ArticleListSerializer, ArticleSerializer
# from .models import Article


# Create your views here.

# def index(request):
#     pass


def book_list(request):
    pass


def book_detail(request, book_pk):
    pass






