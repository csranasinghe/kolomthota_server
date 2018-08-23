from django.conf.urls import url, include
from  django.contrib.auth.views import logout
from .views import login_view, logout_view, index_view
urlpatterns = [
    url('index/$', index_view, name="index"),
    url('login/$', login_view, name="login"),
    url('logout/$', logout, {'next_page': '/accounts/login'},  name="logout")
    # url('logout$', logout_view, name="logout"),
]
