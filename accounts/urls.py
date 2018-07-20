from django.conf.urls import url, include
from .views import login_view, logout_view
urlpatterns = [
    url('login$', login_view, name="login"),
    url('logout$', logout_view, name="logout"),
]
