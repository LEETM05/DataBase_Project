# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.userinfo_edit, name='userinfo_edit'),
#     # path('', views.verify_password, name='verify_password'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    # 회원정보 수정 페이지
    path('', views.userinfo_edit, name='userinfo_edit'),

    # 현재 비밀번호 확인
    path('verify_password/', views.verify_password, name='verify_password'),
    # path('delete_user/', views.delete_user, name='delete_user')
    path('delete_account/', views.delete_account, name='delete_account')
]
