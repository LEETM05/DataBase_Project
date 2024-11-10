from django.urls import path
from camera_page import views

app_name = 'camera_page'

urlpatterns = [
    path('hello_world', views.hello_world, name='hello_world'),
]
