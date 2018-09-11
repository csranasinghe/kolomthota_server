from django.shortcuts import render
from .forms import VesselArrivalDetailsForm
from .models import ShippingLine,VesselArrival


def add_vessel_details(request):
    if request.method == "POST":
         form = VesselArrivalDetailsForm(request.POST)
         if form.is_valid():
             vessel_Detail_item = form.save(commit=False)
             vessel_Detail_item.save()
    else:
        form = VesselArrivalDetailsForm()
    return render( request,'shipping_line/add_vessel_form.html', {'form':form})

def vessel_listview(request):
    if request.method == "POST":
         form = VesselArrivalDetailsForm(request.POST)
         if form.is_valid():
             vessel_Detail_item = form.save(commit=False)
             vessel_Detail_item.save()
    else:
        form = VesselArrivalDetailsForm()
    template_name='shipping_line/vessel_details.html'
    queryset = VesselArrival.objects.all()
    context = {
        "object_list":queryset,
        'form':form
    }
    return render(request, template_name ,context)

def berth_schedule(request):
    template_name='shipping_line/berth_schedule.html'
    context = {

    }
    return render(request, template_name ,context)

def view_history(request):
    template_name='shipping_line/history.html'
    queryset = VesselArrival.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, template_name ,context)