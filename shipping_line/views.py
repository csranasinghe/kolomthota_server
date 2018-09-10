from django.shortcuts import render
from .forms import VesselDetailsForm
from .models import ShippingLine,VesselDetails


def add_vessel_details(request):
    if request.method == "POST":
         form = VesselDetailsForm(request.POST)
         if form.is_valid():
             vessel_Detail_item = form.save(commit=False)
             vessel_Detail_item.save()
    else:
        form = VesselDetailsForm()
    return render( request,'shipping_line/add_vessel_form.html', {'form':form})

def vessel_listview(request):
    template_name='shipping_line/vessel_details.html'
    queryset = VesselDetails.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, template_name ,context)

def berth_schedule(request):
    template_name='shipping_line/berth_schedule.html'
    context = {

    }
    return render(request, template_name ,context)

def view_history(request):
    template_name='shipping_line/history.html'
    queryset = VesselDetails.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, template_name ,context)