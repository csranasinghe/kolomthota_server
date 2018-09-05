from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'berth_planner/dashboard.html', {})


def schedule_published(request):
    return render(request, 'berth_planner/schedule_published.html', {})