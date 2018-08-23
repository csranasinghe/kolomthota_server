from django.conf.urls import url, include
from berth_planner.views import index
urlpatterns = [
    url('^$', index, name="index"),
]
