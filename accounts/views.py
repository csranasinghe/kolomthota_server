from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm ,UserChangeForm ,PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm ,EditProfileForm 
from .models import ShippingAgent,Account
from shipping_line.models import ShippingLine


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
        else:
            return redirect('/')

def view_profile(request):
    queryset = ShippingAgent.objects.filter(account=request.user)
    content = {'user':request.user}
    return render(request,'accounts/profile.html',content)
            
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        content = {'form':form}
        return render(request, 'accounts/edit_profile.html', content)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            return redirect('accounts/change_password.html')
    else:
        form = PasswordChangeForm(user=request.user)
        content = {'form':form}
        return render(request, 'accounts/change_password.html', content)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            data = request.POST.get('email')
            form.save()
            person=Account.objects.filter(email = data)
            company = ShippingLine.objects.all()
            context = {
                'person':person[0],
                'company':company
            }
            return render(request, 'accounts/company_select.html', context)
        else:
            return render(request, 'accounts/register_warning.html', )
    else:
        form = CustomUserCreationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

def register_company(request):
    if request.method == 'GET':
        account_new = request.GET.get('shipping_agent')
        shipping_line_new = request.GET.get('optradio')
        #user = Account.objects.get(id=int(account_new))
        ShippingAgent.objects.create(
            account = Account.objects.get(id=int(account_new)), 
            shipping_line = ShippingLine.objects.get(name=shipping_line_new)
        )
        return HttpResponseRedirect(reverse('accounts:login'))
    
#
# class RegisterSLAView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
