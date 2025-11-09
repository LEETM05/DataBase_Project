from django.urls import path
from login_page import views

urlpatterns = [
    path('', views.login_view, name='login'),  # 기본 경로로 로그인 뷰 연결
    path('register/', views.register_view, name='register'),  # 회원가입 URL
    path('check_username/', views.check_username, name='check_username'),
    # path('logout/', views.custom_logout_view, name='logout'),# 중복 아이디 확인 URL
    # path('logout/', views.logout_func, name='logout_func'),
]