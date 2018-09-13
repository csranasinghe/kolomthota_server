from django.shortcuts import render
from .forms import VesselArrivalDetailsForm,VesselDetailsForm
from .models import ShippingLine,VesselArrival,Vessel




def vessel_listview(request):
    if request.method == "POST":
        form = VesselArrivalDetailsForm(request.POST)
        form_one = VesselDetailsForm(request.POST)
        if form.is_valid():
            vessel_Detail_item = form.save(commit=False)
            vessel_Detail_item.save()
        elif form_one.is_valid():
            vessel_item = form_one.save(commit=False)
            vessel_item.save()
    else:
        form = VesselArrivalDetailsForm()
        form_one = VesselDetailsForm()
    template_name='shipping_line/vessel_details.html'
    queryset = VesselArrival.objects.all()
    context = {
        "object_list":queryset,
        'form':form,
        'form_one':form_one
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