"""
URL configuration for BAA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('accounts/', include('accounts.urls')),
    # path('accounts/', include('dj_rest_auth.urls')), # 이거 나중에 아래로 바꾸기
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/signup/', include('dj_rest_auth.registration.urls')),
    # signup이 아니라.. registration으로 써야한다는데..
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
