# login_page/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import User
import re
from django.http import JsonResponse


# 로그인 뷰 정의
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         # 로그인 검증 로직
#         try:
#             user = User.objects.get(username=username, password=password)
#             messages.success(request, f'안녕하세요, {user.name}님!')
#             return redirect('main_page')  # 로그인 성공 시 메인 페이지로 리다이렉트
#         except User.DoesNotExist:
#             messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
#
#     return render(request, 'login_page/login.html')
#
#
# # 회원가입 뷰 정의
# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         name = request.POST['name']
#
#         # 아이디 유효성 검사 (영어, 숫자만 가능)
#         if not re.match(r'^[a-zA-Z0-9]+$', username):
#             messages.error(request, '아이디는 영어와 숫자만 가능합니다.')
#             return render(request, 'login_page/login.html')
#
#         # 비밀번호 유효성 검사 (영어, 숫자, 특수문자 포함)
#         if not re.match(r'^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$', password):
#             messages.error(request, '비밀번호는 영어, 숫자, 특수문자를 포함해야 하며, 최소 8자 이상이어야 합니다.')
#             return render(request, 'login_page/login.html')
#
#         # 비밀번호 확인
#         if password != confirm_password:
#             messages.error(request, '비밀번호가 일치하지 않습니다.')
#             return render(request, 'login_page/login.html')
#
#         # 사용자 정보 저장
#         try:
#             user = User(username=username, password=password, name=name)
#             user.save()
#             messages.success(request, '회원가입이 완료되었습니다.')
#             return redirect('login')  # 로그인 페이지로 리다이렉트
#         except IntegrityError:
#             messages.error(request, '이미 존재하는 아이디입니다.')
#             return render(request, 'login_page/login.html')
#
#     return render(request, 'login_page/login.html')
#
# def check_username(request):
#     if request.method == 'GET':
#         username = request.GET.get('username', None)
#         if User.objects.filter(username=username).exists():
#             return JsonResponse({'exists': True}, status=200)
#         return JsonResponse({'exists': False}, status=200)

# 로그인 뷰 정의
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # 로그인 검증 로직
        try:
            user = User.objects.get(username=username, password=password)
            messages.success(request, f'안녕하세요, {user.name}님!')
            return redirect('main_page')  # 로그인 성공 시 메인 페이지로 리다이렉트
        except User.DoesNotExist:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')

    return render(request, 'login_page/login.html')

# 회원가입 뷰 정의
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        name = request.POST['name']

        # 아이디 유효성 검사 (영어, 숫자만 가능)
        if not re.match(r'^[a-zA-Z0-9]+$', username):
            messages.error(request, '아이디는 영어와 숫자만 가능합니다.')
            return render(request, 'login_page/login.html')

        # 비밀번호 유효성 검사 (영어, 숫자, 특수문자 포함)
        if not re.match(r'^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$', password):
            messages.error(request, '비밀번호는 영어, 숫자, 특수문자를 포함해야 하며, 최소 8자 이상이어야 합니다.')
            return render(request, 'login_page/login.html')

        # 비밀번호 확인
        if password != confirm_password:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return render(request, 'login_page/login.html')

        # 사용자 정보 저장
        try:
            user = User(username=username, password=password, name=name)
            user.save()
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('login')  # 로그인 페이지로 리다이렉트
        except IntegrityError:
            messages.error(request, '이미 존재하는 아이디입니다.')
            return render(request, 'login_page/login.html')

    return render(request, 'login_page/login.html')

# 중복 아이디 확인 뷰
def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'exists': True}, status=200)
        return JsonResponse({'exists': False}, status=200)