from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def userinfo_page(request):
    return render(request, 'userinfo_page/userinfo_page.html')
