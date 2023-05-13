from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register), # 회원가입 url
    path('login/', views.login), # 로그인 url
    path('logout/', views.logout),
]