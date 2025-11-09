from django.urls import path
from . import views

urlpatterns = [
    # 사용 이력 페이지
    path('', views.history_page, name='history_page'),

    # 특정 약 코드로 결과 페이지
    path('history_result/<str:pill_code>/', views.history_result_page, name='history_result_page'),
    path('delete/', views.delete_history, name='delete_history')
]