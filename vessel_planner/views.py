from django.shortcuts import render ,redirect ,get_object_or_404
from shipping_line.models import VesselArrival
from .models import Messages , VesselProgress
from .forms import MessageSend ,VesselProgressForm
from django.views.generic import UpdateView
from django.http import HttpResponse

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
        dis_new = request.POST.get('dis')
        load_new = request.POST.get('load')
        progress = VesselProgress.objects.get(id=item_id)
        if(dis_new != ""):
            progress.dis = int(dis_new)
        if(load_new != ""):
            progress.load = int(load_new)
        progress.save()
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

