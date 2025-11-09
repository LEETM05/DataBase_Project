from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import os
import torch
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from .models import MedicineInfo, PastHistory
from django.conf import settings
import uuid
import datetime
import json
from django.db import connection

parameter_path = 'C:/Users/tae_min/Desktop/Medicine_project/result_page/best.pt'

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path=parameter_path)

@login_required
def result_page(request):
    image_url = request.GET.get('image_url', '')
    medicine_info_url = request.GET.get('medicine_info_url', '')
    print(image_url)
    return render(request, 'result_page/result_page.html', {
        'image_url': image_url,
        'medicine_info_url': medicine_info_url,
    })


from django.db import connection


@login_required
@csrf_exempt
def process_image(request):
    try:
        # 요청 정보 확인
        print(f"Request method: {request.method}")
        print(f"Request FILES: {request.FILES}")

        if request.method != 'POST':
            return JsonResponse({'error': 'Invalid request method'}, status=405)

        if 'image' not in request.FILES:
            return JsonResponse({'error': 'No image provided in the request'}, status=400)

        # 이미지 저장 및 처리 로직
        image = request.FILES['image']

        # 추가한 부분
        user_id = request.user.id
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        new_image_name = f'{user_id}_{timestamp}.jpg'
        upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads', new_image_name)
        os.makedirs(os.path.dirname(upload_path), exist_ok=True)

        with open(upload_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        print(f"Image saved to: {upload_path}")

        # YOLO 모델 처리
        try:
            results = model(upload_path)
            detections = results.pandas().xyxy[0]
            print(f"YOLO detections: {detections}")
            if detections.empty:
                return JsonResponse({'error': 'No detections found'}, status=400)
            top_detection = detections.sort_values(by='confidence', ascending=False).iloc[0]
            predicted_class = top_detection['name']
            print(f'Predicted_Class : {predicted_class}')

            # SQL SELECT 문 사용
            try:
                with connection.cursor() as cursor:
                    sql = """
                        SELECT 제품코드, 제품명, 효능효과, 용법용량, 저장방법, 사용상의주의사항
                        FROM medicine_info
                        WHERE 제품코드 = %s
                    """
                    cursor.execute(sql, [predicted_class])
                    row = cursor.fetchone()

                if not row:
                    return JsonResponse({'error': 'Medicine info not found'}, status=400)

                # 결과를 딕셔너리로 변환
                medicine_data = {
                    '제품코드': row[0],
                    '제품명': row[1],
                    '효능효과': row[2],
                    '용법용량': row[3],
                    '저장방법': row[4],
                    '사용상의주의사항': row[5],
                }
                print(medicine_data)
            except Exception as e:
                return JsonResponse({'error': f'SQL 처리 실패: {str(e)}'}, status=500)

        except Exception as e:
            print(f"YOLO 처리 실패: {e}")
            return JsonResponse({'error': f'YOLOv5 처리 실패: {str(e)}'}, status=500)

        # JSON 파일 저장
        json_file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f'{user_id}_{timestamp}_medicine.json')
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(medicine_data, json_file, ensure_ascii=False, indent=4)

        # JSON 파일 URL 반환
        json_file_url = f'/media/uploads/{user_id}_{timestamp}_medicine.json'
        return JsonResponse(
            {'message': 'Success', 'image_url': f'/media/uploads/{new_image_name}',
             'medicine_info_url': f'{json_file_url}'},
            status=200)

    except Exception as e:
        print(f"서버 오류: {e}")
        return JsonResponse({'error': f'서버 오류: {str(e)}'}, status=500)

@login_required
@csrf_exempt
def save_history(request):
    """탐지 결과를 past_history 테이블에 SQL로 저장"""
    if request.method == 'POST':
        # 요청에서 데이터 가져오기
        user_id = request.user.id  # 현재 로그인한 사용자 ID
        제품명 = request.POST.get('제품명')
        제품코드 = request.POST.get('제품코드')
        image_url = request.POST.get('image_url')

        if not (user_id and 제품명 and 제품코드 and image_url):
            return JsonResponse({'error': '필수 데이터가 누락되었습니다.'}, status=400)

        try:
            # SQL 실행
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO past_history (id, 제품명, 제품코드, image_url, Date)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, [user_id, 제품명, 제품코드, image_url, now()])

            return JsonResponse({'message': '사용 이력이 저장되었습니다.'}, status=200)

        except Exception as e:
            return JsonResponse({'error': f'SQL 오류: {str(e)}'}, status=500)

    return JsonResponse({'error': '유효하지 않은 요청입니다.'}, status=400)
