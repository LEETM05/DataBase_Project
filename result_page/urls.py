# result_page/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.result_page, name='result_page'),  # 기본 경로로 result.html을 연결
    path('process/', views.process_image, name='process_image'),
    path('api/save_history/', views.save_history, name='save_history'),
]