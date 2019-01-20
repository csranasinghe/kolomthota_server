from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView ,password_reset_done, password_reset ,password_reset_confirm
from .views import AccountLoginView,  IndexView ,register,view_profile
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url('^login/$', AccountLoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(),  name="logout"),
    url('^register/$',register,name='register'),
    url('^profile/$',view_profile,name='viewProfile')
]
