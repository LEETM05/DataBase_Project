from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection  # MySQL 연결을 위한 Django 모듈
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
import json

@login_required
def userinfo_edit(request):
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        # 현재 사용자 가져오기
        user = request.user  # 로그인한 사용자 객체

        # 현재 비밀번호 검증
        if not user.check_password(current_password):  # ORM에서 제공하는 check_password 사용
            messages.error(request, '현재 비밀번호가 올바르지 않습니다.')
            return redirect('userinfo_edit')

        # 새 비밀번호와 확인 비밀번호 일치 여부 검증
        if new_password != confirm_password:
            messages.error(request, '새 비밀번호가 일치하지 않습니다.')
            return redirect('userinfo_edit')

        # 새 비밀번호 유효성 검사
        if len(new_password) < 8 or not any(char.isdigit() for char in new_password) or not any(char.isalpha() for char in new_password):
            messages.error(request, '비밀번호는 최소 8자 이상이어야 하며, 문자와 숫자를 포함해야 합니다.')
            return redirect('userinfo_edit')

        # 비밀번호 업데이트
        user.set_password(new_password)  # set_password로 비밀번호 해싱 및 저장
        user.save()

        messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
        return redirect('userinfo_edit')

    # userinfo_edit.html 렌더링
    return render(request, 'userinfo_edit/userinfo_edit.html', {'user': request.user})

@login_required
def verify_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        current_password = data.get("current_password")

        # 현재 사용자 가져오기
        user = request.user  # 로그인된 사용자 객체

        # 비밀번호 확인
        if user.check_password(current_password):  # Django ORM의 check_password 사용
            return JsonResponse({'success': True})

        return JsonResponse({'success': False})

from django.contrib.auth import authenticate, logout
from django.http import JsonResponse
from django.shortcuts import redirect
from django.db import connection

@login_required
def delete_account(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            password = data.get("delete_password")

            user = request.user
            print(f"POST 요청 도착: {request.body}")
            print(f"사용자 ID: {user.id}, 사용자 이름: {user.password}")
            if user.check_password(password):
                # 명시적으로 SQL 쿼리를 사용하여 삭제
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM user_table WHERE id = %s", [user.id])

                logout(request)
                return JsonResponse({'success': True, 'message': '계정이 성공적으로 삭제되었습니다.'})
            else:
                return JsonResponse({'success': False, 'message': '비밀번호가 올바르지 않습니다.'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': '잘못된 요청 데이터입니다.'})

    return JsonResponse({'success': False, 'message': '잘못된 요청입니다.'})