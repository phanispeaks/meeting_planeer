from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting, Room
# Create your views here.
def welcome(request):
    return render(request,"website/welcome.html",
                  {"meetings":Meeting.objects.all()})


def date(request):
    return HttpResponse("this is present date and time"+str(datetime.now()))