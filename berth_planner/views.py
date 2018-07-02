from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class Login(TemplateView):
    template_name = 'berth_planner/login.html'


def index(request):
    return HttpResponse("<h1>Index page</h1")