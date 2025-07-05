from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('delete/<int:note_id>',views.delete_note,name='delete_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),




]

