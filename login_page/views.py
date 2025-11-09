from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User
import re
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    error_message = None
    if request.method == 'POST':
        user_id = request.POST['username']  # HTML input의 name이 'username'이므로 그대로 사용
        password = request.POST['password']

        # 데이터베이스에서 사용자 정보 확인 및 비밀번호 검증
        try:
            user = User.objects.get(id=user_id)
            if check_password(password, user.password):  # 해싱된 비밀번호 확인
                login(request, user)
                messages.success(request, f'안녕하세요, {user.name}님!')
                return redirect('main_page')  # 로그인 성공 시 메인 페이지로 리다이렉트
            else:
                error_message = '아이디 또는 비밀번호가 올바르지 않습니다.'
        except User.DoesNotExist:
            error_message = '아이디 또는 비밀번호가 올바르지 않습니다.'

    return render(request, 'login_page/login.html', {'error_message': error_message})

# 회원가입 뷰 정의
def register_view(request):
    if request.method == 'POST':
        user_id = request.POST['username']  # HTML input의 name이 'username'이므로 그대로 사용
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        name = request.POST['name']

        # 아이디 유효성 검사 (영어, 숫자만 가능)
        if not re.match(r'^[a-zA-Z0-9]+$', user_id):
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

        # 비밀번호 해싱 후 사용자 정보 저장
        try:
            hashed_password = make_password(password)  # 비밀번호 해싱
            user = User(id=user_id, password=hashed_password, name=name)
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
        user_id = request.GET.get('id', None)  # HTML input의 name이 'username'이므로 그대로 사용
        if User.objects.filter(id=user_id).exists():
            return JsonResponse({'exists': True}, status=200)
        return JsonResponse({'exists': False}, status=200)

# 로그아웃 뷰 정의
def custom_logout_view(request):
    logout(request)  # Django 기본 로그아웃 함수 호출
    request.session.flush()  # 모든 세션 데이터 삭제
    return redirect('login_page/login.html')  # 로그인 페이지로 리다이렉트