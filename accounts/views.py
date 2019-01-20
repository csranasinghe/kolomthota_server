from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm

import logging
logger = logging.getLogger(__name__)


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                logging.info("User " + username + " authenticated.")
            else:
                messages.error(request, 'Your account has been disabled.')
        else:
            messages.add_message(request, messages.INFO, 'Invalid username or password.')
        return super(AccountLoginView, self).post(request)


class IndexView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        if user.user_type == 'SA':
            return HttpResponseRedirect(reverse('shipping_line:index'))
        elif user.user_type == 'BP':
            return HttpResponseRedirect(reverse('berth_planner:index'))
        elif user.user_type == 'ADMIN':
            return HttpResponseRedirect(reverse('admin:index'))
        elif user.user_type == 'VP' or 'BM':
            return HttpResponseRedirect(reverse('vessel_planner:index'))


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            form = CustomUserCreationForm()
            args = {'form': form}
            return render(request, 'accounts/reg_form.html', args)
    else:
        form = CustomUserCreationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

    
#
# class RegisterSLAView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
