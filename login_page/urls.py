from django.urls import path
from login_page import views

urlpatterns = [
    path('', views.login_view, name='login'),             # 기본 경로를 로그인 페이지로 연결
    path('login/', views.login_view, name='login'),       # /login_page/login/ 경로 연결
    path('register/', views.register_view, name='register'),
path('check_username/', views.check_username, name='check_username'),
]