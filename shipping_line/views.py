from django.shortcuts import render
from .forms import VesselArrivalDetailsForm
from .models import ShippingLine,VesselArrival

def index(request):
    return render(request, 'shipping_line/index.html', {})

def addVessel(request):
    return render(request, 'shipping_line/addVesselForm.html', {})

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
    template_name='shipping_line/index.html'
    queryset = VesselArrival.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, template_name ,context)