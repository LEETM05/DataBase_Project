from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse


def history_page(request):
    """
    사용 이력 페이지
    """
    user_id = request.user.id

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 제품코드, 제품명, image_url, Date 
            FROM past_history 
            WHERE id = %s
        """, [user_id])
        rows = cursor.fetchall()

    history = []
    for row in rows:
        pill_code = row[0]
        pill_name = row[1]
        image_url = row[2]
        saved_date = row[3]

        history.append({
            'pill_code': pill_code,
            'pill_name': pill_name,
            'thumbnail_url': image_url + "?size=small",
            'saved_date': saved_date.strftime("%Y-%m-%d %H:%M:%S")
        })

    return render(request, 'history_page/history_page.html', {'history': history})


@login_required
def history_result_page(request, pill_code):
    """
    특정 약 코드에 대한 상세 정보를 표시하는 페이지
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ph.image_url, mi.제품코드, mi.제품명, mi.효능효과, mi.용법용량, mi.저장방법, mi.사용상의주의사항
            FROM past_history ph
            JOIN medicine_info mi ON ph.제품코드 = mi.제품코드
            WHERE ph.제품코드 = %s
        """, [pill_code])
        row = cursor.fetchone()

    if not row:
        return render(request, 'history_page/error_page.html', {'message': f"'{pill_code}'에 해당하는 데이터를 찾을 수 없습니다."})

    context = {
        'image_url': row[0],
        'pill_code': row[1],
        'pill_name': row[2],
        'efficacy': row[3],
        'usage': row[4],
        'storage': row[5],
        'precautions': row[6],
    }

    return render(request, 'history_result_page.html', context)


@login_required
def delete_history(request):
    if request.method == "POST":
        image_url = request.POST.get("image_url").replace('?size=small', '')
        if not image_url:
            return JsonResponse({"error": "image_url is required"}, status=400)
        with connection.cursor() as cursor:
            # 삭제 실행
            cursor.execute("""
                DELETE FROM past_history
                WHERE image_url = %s
            """, [image_url])

        return JsonResponse({"message": "삭제가 완료되었습니다."}, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)
