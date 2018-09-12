from django.http import HttpResponse
from django.shortcuts import render
from shipping_line.models import VesselArrival


def index(request):
    queryset = VesselArrival.objects.filter(is_reviewed=False).count()
    querysetOne = VesselArrival.objects.filter(is_reviewed=False)
    
    context = {
        "object_list":queryset,
        "object_list_data":querysetOne 
    }
    return render(request, 'berth_planner/dashboard.html', context)


def schedule_published(request):
    return render(request, 'berth_planner/schedule_published.html', {})