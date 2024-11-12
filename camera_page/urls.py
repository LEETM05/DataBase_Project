from django.urls import path
from . import views

urlpatterns = [
    path('', views.camera_page, name='camera_page'),  # 기본 경로로 camera_page.html을 연결
]