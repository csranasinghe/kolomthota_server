from django.conf.urls import url, include
from django.contrib.auth.views import (
    LogoutView ,
    PasswordResetView ,
    PasswordResetDoneView
)
from .views import (
    AccountLoginView,  
    IndexView ,
    register ,
    view_profile ,
    edit_profile ,
    change_password,
    register_company
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url('^login/$', AccountLoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(),  name="logout"),
    url('^register/$',register,name='register'),
    url('^profile/$',view_profile,name='viewProfile'),
    url('^profile/edit/$',edit_profile ,name = "editProfile" ),
    url('^change-password/$', change_password ,name = "changePassword" ),
    url('^register/company/$', register_company, name = "register_company")
]
