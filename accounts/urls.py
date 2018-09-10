from django.conf.urls import url, include
from  django.contrib.auth.views import logout
from .views import login_view, logout_view, index_view
urlpatterns = [
    # url('^', index_view, name="index"),
    url(r'^$', index_view, name="index"),
    url('^login/$', login_view, name="login"),
    url('^logout/$', logout, {'next_page': '/login'},  name="logout")

]
