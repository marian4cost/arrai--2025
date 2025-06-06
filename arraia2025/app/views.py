from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def vote_king(request):
    return render(request, "vote_king.html")

def vote_queen(request):
    return render(request, "vote_queen.html")

def candidates(request):
    return render(request, "candidates.html")