from django.urls import path
from . import views

urlpatterns = [
    path('', views.history_page, name='history_page'),  # 사용 이력 페이지
    # path('result/<str:pill_code>/', views.result_page, name='result_page'),  # 특정 약 코드로 결과 페이지
]