from django.shortcuts import render

# Create your views here.

def userinfo_page(request):
    return render(request, 'userinfo_page/userinfo_page.html')
