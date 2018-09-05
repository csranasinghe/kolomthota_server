from django.conf.urls import url, include
from .views import index, schedule_published
urlpatterns = [
    url('^$', index, name="index"),
    url('^schedule/published$', schedule_published, name="schedule_published"),
]
