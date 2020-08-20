from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404 ,redirect
from shipping_line.models import VesselArrival
from .models import BerthAllocation

def index(request):
    queryset = VesselArrival.objects.filter(is_scheduled=False, is_rejected_user=False, is_reviewed=True).order_by('-eta')
    context = {
        "vessel_arrivals": queryset,
    }
    return render(request, 'berth_planner/dashboard.html', context)


def schedule_published(request):
    result = BerthAllocation.objects.latest('id')
    schedule_list = result.schedule_details.get('va_list')

    return render(request, 'berth_planner/schedule_published.html', {'berth_allocation': result, 'schedule_list': schedule_list})


def vessel_arrivals(request):
    vessels = VesselArrival.objects.filter(is_scheduled=False).order_by('-eta')
    return render(request, 'berth_planner/vessel_arrivals.html', {"vessels": vessels})


def vessel_arrivals_review(request, id, review_status):
    if request.user.user_type == 'BP':
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
    else:
        return JsonResponse(data={}, status=401)