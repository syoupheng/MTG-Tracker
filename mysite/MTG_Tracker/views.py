from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'MTG_Tracker/index.html')