from django.shortcuts import render ,redirect
from shipping_line.models import VesselArrival
from .models import Messages , VesselProgress
from .forms import MessageSend ,VesselProgressForm

# Create your views here.
def vessel_dashboard(request):
    if request.method == "POST":
        form = MessageSend(request.POST)
        form_one = VesselProgressForm(request.POST)
        if form.is_valid():
            form.save()
        elif form_one.is_valid():
            form_one.save()
    else:
        form = MessageSend()
        form_one = VesselProgressForm()
    
    queryset = VesselProgress.objects.all()
    template_name='vessel_planner/dashboard.html'
    context = {
        'form':form,
        "object_list":queryset,
        'form_one':form_one
    }
    return render(request,template_name,context)

def progress(request,item_id=None):
    if request.method == "POST":
        form_value = VesselProgressForm(request.POST)
        
        if form_value.is_valid():
            progress = VesselProgress.objects.get(id=item_id)
            form_value = VesselProgressForm(request.POST, instance = progress)
            form_value.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        progress = VesselProgress.objects.get(id=item_id)
        form_value = VesselProgressForm(instance = progress)
        template_name='vessel_planner/edit_details.html'
        context = {
            'progress':progress,
            'form':form_value
        }
        return render(request, template_name ,context)

def remove_vessel_progress(request,item_id=None):
    item = VesselProgress.objects.get(id=item_id)       
    item.delete()
    return redirect('/')