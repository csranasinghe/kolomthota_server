from django.shortcuts import render
from .forms import VesselDetailsForm
from .models import ShippingLine,VesselDetails

def index(request):
    return render(request, 'shipping_line/index.html', {})

def addVessel(request):
    return render(request, 'shipping_line/addVesselForm.html', {})

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
    template_name='shipping_line/index.html'
    queryset = VesselDetails.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, template_name ,context)