# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
# from .models import History  # History 모델 가져오기

@login_required
def history_page(request):
    # 현재 사용자의 이력 가져오기
    # user_history = History.objects.filter(user=request.user).order_by('-saved_date')  # 최신 순 정렬
    # return render(request, 'history_page/history_page.html', {'history': user_history})
    return render(request, 'history_page/history_page.html')

# @login_required
# def result_page(request, pill_code):
#     # result_page는 이미 구현되어 있다고 가정합니다.
#     # pill_code를 통해 약 정보를 가져와 사용자에게 보여줍니다.
#     pass