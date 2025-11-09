from django.urls import path
from result_page.views import process_image  # result_page의 process_image를 import
from camera_page.views import camera_page  # 절대 경로로 views 가져오기

urlpatterns = [
    path('process/', process_image, name='process_image'),  # 'process/' URL을 process_image 뷰에 연결
    path('', camera_page, name='camera_page')
]