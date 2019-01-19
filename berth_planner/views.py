from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404 ,redirect
from shipping_line.models import VesselArrival
from vessel_planner.models import Messages


def index(request):
    queryset = VesselArrival.objects.filter(is_reviewed=True).order_by('-eta')

    context = {
        "vessel_arrivals":queryset,
    }
    return render(request, 'berth_planner/dashboard.html', context)

def show_messages(request):
    queryset1 = Messages.objects.filter(is_reviewed=False)
    queryset2 = Messages.objects.filter(is_reviewed=True)

    context = {
        "messages1":queryset1,
        "messages2":queryset2,
    }
    return render(request, 'berth_planner/messages.html', context)

def mark_as_read(request,item_id=None):
    item = Messages.objects.get(id=item_id)       
    item.is_reviewed = True
    item.save()
    return redirect('/berth-planner/messages')

def mark_as_unread(request,item_id=None):
    item = Messages.objects.get(id=item_id)       
    item.is_reviewed = False
    item.save()
    return redirect('/berth-planner/messages')


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