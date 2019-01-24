from django.shortcuts import render,redirect
from .forms import VesselArrivalDetailsForm,VesselDetailsForm
from .models import ShippingLine,VesselArrival,Vessel




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
    queryset = VesselArrival.objects.filter(shipping_agent=request.user.id)
    context = {
        "object_list":queryset,
        'form':form,
        'form_one':form_one
    }
    return render(request, template_name ,context)

def vessel_timestamp(request):
    template_name='shipping_line/vessel_timestamp.html'
    queryset = VesselArrival.objects.filter(shipping_agent=request.user.id)
    context = {
        "object_list":queryset
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
    template_name='shipping_line/history.html'
    queryset = VesselArrival.objects.all(shipping_line=request.user.sa_account.shipping_line)
    context = {
        "object_list":queryset
    }
    return render(request, template_name ,context)