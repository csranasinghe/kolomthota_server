from django.shortcuts import render,redirect
from .forms import VesselArrivalDetailsForm,VesselDetailsForm
from .models import ShippingLine,VesselArrival,Vessel
from datetime import datetime
from datetime import timedelta
from django.http import HttpResponse




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
    context = {
        "object_list":queryset,
        'form':form,
        'form_one':form_one
    }
    return render(request, template_name ,context)

def vessel_timestamp(request):
    template_name='shipping_line/vessel_timestamp.html'
    queryset = VesselArrival.objects.filter(shipping_agent=request.user.id).order_by('-eta')
    context = {
        "object_list":queryset,
        'time':datetime.now()
    }
    return render(request, template_name ,context)


def remove_arrival(request,item_id=None):
    item = VesselArrival.objects.get(id=item_id)       
    item.delete()
    return redirect('/')

def edit_arrival(request,item_id=None):
    if request.method == "POST":
        form_value = VesselArrivalDetailsForm(request.POST)
        if form_value.is_valid():
            vessel = VesselArrival.objects.get(id=item_id)
            form_value = VesselArrivalDetailsForm(request.POST, instance = vessel)
            form_value.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        vessel = VesselArrival.objects.get(id=item_id)
        form_value = VesselArrivalDetailsForm(instance = vessel)
        template_name='shipping_line/edit_details.html'
        context = {
            'vessel':vessel,
            'form':form_value
        }
        return render(request, template_name ,context)




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

def get_list_to_be_notified():
    pass