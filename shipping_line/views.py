from django.shortcuts import render,redirect
from .forms import VesselArrivalDetailsForm,VesselDetailsForm
from .models import ShippingLine,VesselArrival,Vessel
from datetime import datetime
from datetime import timedelta
from django.http import HttpResponse

def get_list_to_be_notified(queryset):
    time = datetime.now()
    within_72h = []
    within_48h = []
    within_24h = []
    count = 0
    for i in queryset:
        absolute_date = datetime(
                day = i.eta.day,
                month = i.eta.month,
                year = i.eta.year,
                hour = i.eta.hour,
                minute = i.eta.minute
        )
        difference = absolute_date - time
        if i.first_confirm != True :
            if difference.days < 3:
                item = VesselArrival.objects.get(id=i.id)       
                item.delete()
            else:
                within_72h.append(i)
                count += 1
        elif i.second_confirm != True :
            if difference.days < 2:
                item = VesselArrival.objects.get(id=i.id)       
                item.delete()
            else:
                within_48h.append(i)
                count += 1
        elif i.third_confirm != True :
            if difference.days < 1:
                item = VesselArrival.objects.get(id=i.id)       
                item.delete()
            else:
                within_24h.append(i)
                count += 1
    return within_72h, within_48h, within_24h, count

def get_count(queryset):
    within_72h, within_48h, within_24h, count = get_list_to_be_notified(queryset)
    return count

def vessel_listview(request):
    if request.method == "POST":
        form = VesselArrivalDetailsForm(request.POST)
        form_one = VesselDetailsForm(request.POST)
        if form.is_valid():
            form.save()
        elif form_one.is_valid():
            form_one.save()
    else:
        form = VesselArrivalDetailsForm()
        form_one = VesselDetailsForm()
    
    template_name='shipping_line/vessel_details.html'
    queryset = VesselArrival.objects.filter(shipping_agent=request.user.id).order_by('-eta')
    count = get_count(queryset)
    context = {
        "object_list":queryset,
        'form':form,
        'form_one':form_one,
        'count' : count
    }
    return render(request, template_name ,context)

def notification(request):
    pass


def remove_arrival(request,item_id=None):
    item = VesselArrival.objects.get(id=item_id)       
    item.delete()
    return redirect('/')

def edit_arrival(request,item_id=None):
    vessel = VesselArrival.objects.get(id=item_id)
    form_value = VesselArrivalDetailsForm(instance = vessel)
    template_name='shipping_line/edit_details.html'
    context = {
       'vessel':vessel,
        'form':form_value
    }
    return render(request, template_name ,context)

#this must be taken from chamath
def berth_schedule(request):
    template_name='shipping_line/berth_schedule.html'
    context = {

    }
    return render(request, template_name ,context)


def view_history(request):
    if request.method=="GET":
        data = request.GET.get('from_date')
        data_limit = request.GET.get('to_date')

        start = datetime(
            day = int(data[8:10]),
            month = int(data[5:7]),
            year = int(data[0:4]),
            hour = int(data[11:13]),
            minute = int(data[14:])
        )
        end = datetime(
            day = int(data_limit[8:10]),
            month = int(data_limit[5:7]),
            year = int(data_limit[0:4]),
            hour =  int(data_limit[11:13]),
            minute = int(data_limit[14:])
        )
        #remainder = end - start
        queryset = VesselArrival.objects.all().order_by('-eta')
        value_in_queryset=[]
        for i in queryset:
            absolute_date = datetime(
                day = i.eta.day,
                month = i.eta.month,
                year = i.eta.year,
                hour = i.eta.hour,
                minute = i.eta.minute
            )
            if start <= absolute_date <=end :
                value_in_queryset.append(i)
            else:
                pass

        template_name='shipping_line/history.html'
        context = {
            "object_list":value_in_queryset
        }
        return render(request, template_name ,context)


def vessel_timestamp(request):
    template_name='shipping_line/vessel_timestamp.html'
    time = datetime.now()
    queryset = VesselArrival.objects.filter(shipping_agent=request.user.id).order_by('-eta')
    within_72h = []
    within_48h = []
    within_24h = []
    for i in queryset:
        absolute_date = datetime(
                day = i.eta.day,
                month = i.eta.month,
                year = i.eta.year,
                hour = i.eta.hour,
                minute = i.eta.minute
        )
        difference = absolute_date - time
        if i.first_confirm != True :
            if difference.days < 3:
                item = VesselArrival.objects.get(id=i.id)       
                item.delete()
            else:
                within_72h.append(i)
        elif i.second_confirm != True :
            if difference.days < 2:
                item = VesselArrival.objects.get(id=i.id)       
                item.delete()
            else:
                within_48h.append(i)
        elif i.third_confirm != True :
            if difference.days < 1:
                item = VesselArrival.objects.get(id=i.id)       
                item.delete()
            else:
                within_24h.append(i)
         
        
    context = {
        "object_list":queryset,
        'time':datetime.now(),
        'obj' :within_72h
    }
    return render(request, template_name ,context)

def edit_arrival_done(request,item_id=None):
    if request.method=="GET":
        eta_new = request.GET.get('eta')
        dis_new = request.GET.get('dis')
        load_new = request.GET.get('load')
        draft_arrival_new = request.GET.get('draft_arrival')
        draft_departure_new = request.GET.get('draft_departure')
        service_new = request.GET.get('service')
        
        vessel = VesselArrival.objects.get(id=item_id)
        if(eta_new != ""):
            eta_datetime = datetime(
                day = int(eta_new[8:10]),
                month = int(eta_new[5:7]),
                year = int(eta_new[0:4]),
                hour = int(eta_new[11:13]),
                minute = int(eta_new[14:16])
            )
            vessel.eta = eta_datetime
        if(dis_new != "" ):
            vessel.dis = int(dis_new)
        if(load_new != "" ):
            vessel.load = int(load_new)
        if(draft_arrival_new != ""):
            vessel.draft_arrival = float(draft_arrival_new)
        if(draft_departure_new != ""):
            vessel.draft_departure = float(draft_departure_new)
        if(service_new != ""):
            vessel.service = service_new
        vessel.save()

    return redirect('/')