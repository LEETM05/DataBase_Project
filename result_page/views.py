from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def result_page(request):
    return render(request, 'result_page/result_page.html')