from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

@login_required
def topic_list(request):
    if request.method=="POST":
        form=TopicForm(request.POST)
        if form.is_valid():
            topic=form.save(commit=False)
            topic.user=request.user
            topic.save()
            messages.success(request,'Topic added successfully!')
            return redirect ('topic_list')
    else:
        form=TopicForm()
    
    topics=Topic.objects.filter(user=request.user).order_by('-created_at')
    paginator=Paginator(topics,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request, 'revision/topic_list.html', {'form': form, 'page_obj': page_obj})
