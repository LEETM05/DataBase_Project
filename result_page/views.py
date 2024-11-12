from django.shortcuts import render

# Create your views here.
def result_page(request):
    return render(request, 'result_page/result_page.html')