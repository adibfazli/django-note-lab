from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/' , views.NoteList.as_view() , name='notes'),
    path('notes/add/' , views.NoteCreate.as_view() , name='note_add'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='notes_delete'),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='notes_update'),
    path('notes/<int:note_id>/' , views.note_detail , name='note_detail'),
    path('accounts/signup', views.signup, name='signup'),
]