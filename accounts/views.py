from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, reverse

import logging
logger = logging.getLogger(__name__)


def login_view(request):
    template = 'accounts/login.html'
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts:index'))
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, template, {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                logging.info("User "+username+" authenticated.")
                login(request, user)
                return HttpResponseRedirect(reverse('accounts:index'))
            else:
                logging.info("User " + username + " authenticated.")
        else:
            return render(request, template, {'form': form, 'errors': {}})


def logout_view(request):
    logout(request)
    return HttpResponse("Logged out")


@login_required
def index_view(request):
    # return HttpResponse("Accouonts index")
    u = request.user
    if request.user.user_type == 'SA':
        return HttpResponseRedirect(reverse('shipping_line:index'))
    elif request.user.user_type == 'BP':
        return HttpResponseRedirect(reverse('berth_planner:index'))
