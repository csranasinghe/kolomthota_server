from django.conf.urls import url
from .views import vessel_details

urlpatterns = [
    url(r'^vessels$',  vessel_details, name="vessel_details"),


]
