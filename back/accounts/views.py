from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

# serialize 전 코드
# @login_required
# def follow(request, user_pk):
#     User = get_user_model()
#     person = User.objects.get(pk=user_pk)
#     if person != request.user:
#         if request.user in person.followers.all():
#             person.followers.remove(request.user)
#         else:
#             person.followers.add(request.user)
#     return redirect('accounts:profile', person.username)




