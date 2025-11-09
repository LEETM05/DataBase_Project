"""
URL configuration for Medicine_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('login_page/', include('login_page.urls')),  # login_page URL 연결
#     path('camera_page/', include('camera_page.urls')),
#     path('main_page/', include('main_page.urls')),    # main_page URL 연결
#     path('result_page/', include('result_page.urls')),
#     # path('main_page/result/', include('result_page.urls')),  # 결과 페이지를 main_page/result 경로로 연결
#     path('', lambda request: redirect('/login_page/')),  # 기본 루트 경로를 login으로 리다이렉트
#     path('userinfo_page/', include('userinfo_page.urls')),
#     path('infoedit_page/', include('infoedit_page.urls')),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_page/', include('login_page.urls')),  # login_page URL 연결
    path('camera_page/', include('camera_page.urls')),
    path('main_page/', include('main_page.urls')),  # main_page URL 연결
    path('result_page/', include('result_page.urls')),
    path('userinfo_page/', include('userinfo_page.urls')),
    # 기본 루트 경로를 login_page로 리다이렉트
    path('', lambda request: redirect('login')),  # 'login'은 login_page.urls에서 설정한 URL name입니다.
    path('userinfo_edit/', include('userinfo_edit.urls')),
    path('history_page/', include('history_page.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)