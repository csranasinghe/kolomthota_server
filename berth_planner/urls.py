from django.conf.urls import url, include
from berth_planner.views import Login, index
urlpatterns = [
    url('^login$', Login.as_view(), name='berth_planner_login'),
    url('^$', index, name="berth_planner_index"),
]
