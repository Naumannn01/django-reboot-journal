from django.shortcuts import render, redirect, HttpResponse # type: ignore
from .models import Note
from .forms import NoteForm
from django.contrib import messages
from django.shortcuts import get_object_or_404





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

def delete_note(request,note_id):
    note=get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('home')

def about(request):
    return HttpResponse("About" )