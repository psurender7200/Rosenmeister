from django.contrib import admin
from django.urls import path,include

from RosenmeisterApp import views_user_birthday
from rest_framework.routers import DefaultRouter
from RosenmeisterApp import views_Letter_digit

router = DefaultRouter()
router.register(r'birthday', views_user_birthday.user_birthday, basename='data')

urlpatterns = [
    path("",include(router.urls)),
    path("letterdigit/",views_Letter_digit.Letter_digit.as_view())
]