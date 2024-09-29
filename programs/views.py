from django.shortcuts import render

def index(request):
    return render(request, 'programs/programs-main.html')