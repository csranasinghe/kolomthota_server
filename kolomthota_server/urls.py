"""kolomthota_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import (
    PasswordResetView ,
    PasswordResetDoneView ,
    PasswordResetConfirmView ,
    PasswordResetCompleteView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^chat/', include('chat.urls')),
    url(r'^berth-planner/', include('berth_planner.urls', namespace="berth_planner")),
    url(r'^shipping-line/', include('shipping_line.urls', namespace="shipping_line")),
    url(r'^vessel-planner/', include('vessel_planner.urls', namespace="vessel_planner")),
    url(r'^api/', include('mobile_api.urls', namespace="api")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^password-reset/$', 
        PasswordResetView.as_view(
            template_name='accounts/password_reset.html'
            ), 
        name='password_reset'
    ),
    url(r'^password-reset/done/$', 
        PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
            ), 
        name='password_reset_done'
    ),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'
            ), 
        name='password_reset_confirm'
    ),
    url(r'^password-reset-complete/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
            ), 
        name='password_reset_complete'
    ),


]
