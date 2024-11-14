# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.hashers import check_password
# import MySQLdb
# import os
#
# from django.http import JsonResponse
#
#
# @login_required
# def userinfo_edit(request):
#     if request.method == "POST":
#         current_password = request.POST.get("current_password")
#         new_password = request.POST.get("new_password")
#         confirm_password = request.POST.get("confirm_password")
#
#         username = request.user.username
#
#         # Connect to the MySQL database
#         db = MySQLdb.connect(
#             host="localhost",
#             user="taemin",
#             passwd="dkdrlahEl0520!",
#             db="medicinedb",
#             port=3306
#         )
#         cursor = db.cursor()
#
#         # Get the current password for the user from the database
#         cursor.execute("SELECT password FROM login_page_user WHERE username = %s", [username])
#         db_password = cursor.fetchone()[0]
#
#         # Check if current password is correct
#         if not check_password(current_password, db_password):
#             messages.error(request, "현재 비밀번호가 다릅니다.")
#             return render(request, "userinfo_edit.html")
#
#         # Check if new passwords match
#         if new_password != confirm_password:
#             messages.error(request, "새 비밀번호가 일치하지 않습니다.")
#             return render(request, "userinfo_edit.html")
#
#         # Update password
#         cursor.execute("UPDATE login_page_user SET password = %s WHERE username = %s", [new_password, username])
#         db.commit()
#         db.close()
#
#         messages.success(request, "비밀번호가 성공적으로 변경되었습니다.")
#         return redirect("userinfo_edit")
#
#     return render(request, "userinfo_edit.html")
#
# @login_required
# def verify_password(request):
#     if request.method == "POST":
#         current_password = request.POST.get("current_password")
#         username = request.user.username
#
#         # MySQL 데이터베이스에 연결
#         db = MySQLdb.connect(
#             host="127.0.0.1",
#             user="taemin",
#             passwd="dkdrlahEl0520!",
#             db="medicinedb",
#             port=3306
#         )
#         cursor = db.cursor()
#
#         # 현재 비밀번호 가져오기
#         cursor.execute("SELECT password FROM login_page_user WHERE username = %s", [username])
#         db_password = cursor.fetchone()[0]
#         db.close()
#
#         # 현재 비밀번호 확인
#         if current_password == db_password:
#             return JsonResponse({"valid": True})
#         else:
#             return JsonResponse({"valid": False})
#     return JsonResponse({"error": "Invalid request"}, status=400)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import MySQLdb

# @login_required
# def userinfo_edit(request):
#     if request.method == "POST":
#         # AJAX 비밀번호 확인 요청일 경우
#         # if request.is_ajax() and request.POST.get("action") == "verify_password":
#         if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.POST.get("action") == "verify_password":
#             current_password = request.POST.get("current_password")
#             username = request.user.username
#
#             # MySQL 데이터베이스에 연결
#             db = MySQLdb.connect(
#                 host="127.0.0.1",
#                 user="taemin",
#                 passwd="dkdrlahEl0520!",
#                 db="medicinedb",
#                 port=3306
#             )
#             cursor = db.cursor()
#
#             # 현재 비밀번호 가져오기
#             cursor.execute("SELECT password FROM login_page_user WHERE username = %s", [username])
#             db_password = cursor.fetchone()[0]
#             db.close()
#
#             # 비밀번호 확인 결과 반환
#             if current_password == db_password:
#                 return JsonResponse({"valid": True})
#             else:
#                 return JsonResponse({"valid": False})
#
#         # 비밀번호 변경 요청일 경우
#         else:
#             current_password = request.POST.get("current_password")
#             new_password = request.POST.get("new_password")
#             confirm_password = request.POST.get("confirm_password")
#             username = request.user.username
#
#             # MySQL 데이터베이스에 연결
#             db = MySQLdb.connect(
#                 host="localhost",
#                 user="taemin",
#                 passwd="dkdrlahEl0520!",
#                 db="medicinedb",
#                 port=3306
#             )
#             cursor = db.cursor()
#
#             # 현재 비밀번호 확인
#             cursor.execute("SELECT password FROM login_page_user WHERE username = %s", [username])
#             db_password = cursor.fetchone()[0]
#
#             if current_password != db_password:
#                 messages.error(request, "현재 비밀번호가 다릅니다.")
#                 db.close()
#                 return render(request, "userinfo_edit.html")
#
#             # 새 비밀번호와 확인 비밀번호가 일치하는지 확인
#             if new_password != confirm_password:
#                 messages.error(request, "새 비밀번호가 일치하지 않습니다.")
#                 db.close()
#                 return render(request, "userinfo_edit.html")
#
#             # 비밀번호 업데이트
#             cursor.execute("UPDATE login_page_user SET password = %s WHERE username = %s", [new_password, username])
#             db.commit()
#             db.close()
#
#             messages.success(request, "비밀번호가 성공적으로 변경되었습니다.")
#             return redirect("userinfo_edit")
#
#     return render(request, "userinfo_edit.html")

from django.contrib.auth.hashers import check_password

@login_required
def userinfo_edit(request):
    if request.method == "POST":
        # AJAX 비밀번호 확인 요청일 경우
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.POST.get("action") == "verify_password":
            current_password = request.POST.get("current_password")
            username = request.user.username

            # MySQL 데이터베이스에 연결
            db = MySQLdb.connect(
                host="127.0.0.1",
                user="taemin",
                passwd="dkdrlahEl0520!",
                db="medicinedb",
                port=3306
            )
            cursor = db.cursor()

            # 현재 비밀번호 가져오기
            cursor.execute("SELECT password FROM login_page WHERE username = %s", [username])
            db_password = cursor.fetchone()[0]
            db.close()

            # 비밀번호 확인 결과 반환 (check_password 사용)
            if check_password(current_password, db_password):
                return JsonResponse({"valid": True})
            else:
                return JsonResponse({"valid": False})

        # 비밀번호 변경 요청일 경우
        else:
            current_password = request.POST.get("current_password")
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")
            username = request.user.username

            # 비밀번호 값이 None이거나 빈 문자열인지 확인
            if not current_password or not new_password or not confirm_password:
                messages.error(request, "모든 비밀번호 필드를 입력해야 합니다.")
                return render(request, "userinfo_edit.html")

            # MySQL 데이터베이스에 연결
            db = MySQLdb.connect(
                host="localhost",
                user="taemin",
                passwd="dkdrlahEl0520!",
                db="medicinedb",
                port=3306
            )
            cursor = db.cursor()

            # 현재 비밀번호 확인
            cursor.execute("SELECT password FROM login_page WHERE username = %s", [username])
            db_password = cursor.fetchone()[0]

            if not check_password(current_password, db_password):
                messages.error(request, "현재 비밀번호가 다릅니다.")
                db.close()
                return render(request, "userinfo_edit.html")

            # 새 비밀번호와 확인 비밀번호가 일치하는지 확인
            if new_password != confirm_password:
                messages.error(request, "새 비밀번호가 일치하지 않습니다.")
                db.close()
                return render(request, "userinfo_edit.html")

            # 비밀번호 업데이트 - 비밀번호가 비어 있지 않은지 확인
            if new_password.strip() == "":
                messages.error(request, "새 비밀번호를 올바르게 입력해야 합니다.")
                db.close()
                return render(request, "userinfo_edit.html")

            # 비밀번호를 해시하여 업데이트
            from django.contrib.auth.hashers import make_password
            hashed_password = make_password(new_password)
            cursor.execute("UPDATE login_page SET password = %s WHERE username = %s", [hashed_password, username])
            db.commit()
            db.close()

            messages.success(request, "비밀번호가 성공적으로 변경되었습니다.")
            return redirect("userinfo_edit")

    return render(request, "userinfo_edit.html")
