from django.shortcuts import render, HttpResponse # type: ignore
from . models import Note


def home(request):
    notes=Note.objects.all().order_by('created_at')
    return render(request,'home.html',{"notes":notes})

def about(request):
    return HttpResponse("About" )