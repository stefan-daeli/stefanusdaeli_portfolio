from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def en_home(request):
    return render(request, 'en_home.html')
