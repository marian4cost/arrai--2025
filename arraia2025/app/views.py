from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def candidate01(request):
    return render(request, "candidate01.html")