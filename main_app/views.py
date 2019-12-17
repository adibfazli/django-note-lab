from django.shortcuts import render , redirect
from .models import Note
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
    return render(request, 'home.html')

def notes(request):
    notes = Note.objects.all()
    return render(request , 'notes/index.html' , {'notes': notes})

def note_add(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    note = Note(title=title ,content=content)
    note.save()
    return redirect('notes')

class NoteDelete(DeleteView):
    model = Note
    success_url = 'notes/'
