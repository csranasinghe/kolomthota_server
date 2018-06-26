from django.conf.urls import url, include
from berth_planner.views import login
urlpatterns = [
    url('^$', login),
]
