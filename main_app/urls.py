from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/' , views.notes , name='notes'),
    path('notes/add/' , views.note_add , name='note_add'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='notes_delete'),
]