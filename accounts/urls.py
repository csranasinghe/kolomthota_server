from django.conf.urls import url, include
from  django.contrib.auth.views import LogoutView
from .views import AccountLoginView,  IndexView
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url('^login/$', AccountLoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(),  name="logout")

]
