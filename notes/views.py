from django.shortcuts import render, redirect, HttpResponse # type: ignore
from .models import Note
from .forms import NoteForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def home(request):


    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Note added successfully!')
            return redirect('home')
            
    note_list = Note.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(note_list, 5)  # 5 notes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'form': form, 'page_obj': page_obj})


def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=UserCreationForm()
    
    return render(request,'signup.html',{'form':form})


def edit_note(request,note_id):
    note=get_object_or_404(Note,id=note_id)

    if request.method=="POST":
        form=NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            messages.success(request,"Note updated successfully")
            return redirect('home')
    else:
        form=NoteForm(instance=note)
    return render(request,'edit.html',{'form':form,'note':note})


def delete_note(request,note_id):
    note=get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('home')

def about(request):

    return HttpResponse("About" )


def logout_view(request):
    logout(request)
    return redirect('login')