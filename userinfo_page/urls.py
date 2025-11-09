# userinfo_page/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.userinfo_page, name='userinfo_page'),  # 기본 경로로 userinfo_page.html을 연결
    # path('edit-profile/', views.edit_profile, name='edit_profile'),  # 회원정보 수정 페이지
    # path('history/', views.history, name='history'),  # 과거 이력 페이지
]