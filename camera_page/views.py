from django.shortcuts import render

# Create your views here.
# camera_page/views.py
from django.shortcuts import render

def camera_page(request):
    return render(request, 'camera_page/camera_page.html')