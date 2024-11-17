from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
# camera_page/views.py
from django.shortcuts import render

@login_required
def camera_page(request):
    return render(request, 'camera_page/camera_page.html')