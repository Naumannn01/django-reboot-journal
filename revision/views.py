from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import paginator
from django.contrib import messages

