from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404 ,redirect
from shipping_line.models import VesselArrival


def index(request):
    queryset = VesselArrival.objects.filter(is_reviewed=True).order_by('-eta')
    context = {
        "vessel_arrivals": queryset,
    }
    return render(request, 'berth_planner/dashboard.html', context)


def schedule_published(request):
    return render(request, 'berth_planner/schedule_published.html', {})


def vessel_arrivals(request):
    vessels = VesselArrival.objects.all().order_by('-eta')
    return render(request, 'berth_planner/vessel_arrivals.html', {"vessels": vessels})


def vessel_arrivals_review(request, id, review_status):
    sub = get_object_or_404(VesselArrival, id=id)
    status = 200
    if review_status == 'approve':
        sub.is_reviewed = True
        sub.save()
    elif review_status == 'reject':
        sub.is_reviewed = False
        sub.save()
    else:
        status = 400
    return JsonResponse(data={},status=status)