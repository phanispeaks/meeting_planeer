from django.shortcuts import render,get_object_or_404,redirect

# from django.forms import modelform_factory
from .models import Meeting,Room
from .forms import MeetingForm
# Create your views here.

def detail(request,id):
    #meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting,pk=id)
    return render(request,"meetings/details.html",{"meeting":meeting})

def experiment(request,id):
    meeting = Meeting.objects.get(title=id)
    return render(request,"meetings/details.html",{"meeting":meeting})

def room_list(request):
    return render(request,"meetings/room_list.html",
                  {"rooms":Room.objects.all()})

#MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request,'meetings/new.html',{"form":form})
