from django.shortcuts import render, HttpResponse # type: ignore
from .models import Note
from .forms import NoteForm



def home(request):
    notes=Note.objects.all().order_by('created_at')
    
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=NoteForm()


    return render(request,'home.html',{'form':form,"notes":notes})

def about(request):
    return HttpResponse("About" )