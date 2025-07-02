from django.shortcuts import render, redirect, HttpResponse # type: ignore
from .models import Note
from .forms import NoteForm
from django.contrib import messages




def home(request):
    notes=Note.objects.all().order_by('created_at')
    
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Note added successfully")
            return redirect('home')
    else:
        form=NoteForm()


    return render(request,'home.html',{'form':form,"notes":notes})

def about(request):
    return HttpResponse("About" )