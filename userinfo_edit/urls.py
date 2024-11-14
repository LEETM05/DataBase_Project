from django.urls import path
from . import views

urlpatterns = [
    path('', views.userinfo_edit, name='userinfo_edit'),
    # path('', views.verify_password, name='verify_password'),
]
