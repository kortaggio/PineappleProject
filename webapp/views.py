from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def mobile(request):
    return render(request, 'mobile.html')