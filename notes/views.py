from django.shortcuts import render, HttpResponse # type: ignore

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the notes home.")