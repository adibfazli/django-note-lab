from django.shortcuts import render , redirect
from .models import Note
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
  
def home(request):
    return render(request, 'home.html')

class NoteList(LoginRequiredMixin, ListView):
    def get_queryset(self):
      return Note.objects.filter(user=self.request.user)


class NoteCreate(LoginRequiredMixin,CreateView):
    model = Note
    fields = ['title' , 'content' , 'status']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # note = Note(title=title ,content=content)
    # note.save()
    # return redirect('notes')

@login_required
def note_detail(request , note_id):
    note = Note.objects.get(id=note_id)
    return render(request , 'notes/detail.html' , {'note' : note})


class NoteDelete(LoginRequiredMixin,DeleteView):
    model = Note
    success_url = '/notes/'


class NoteUpdate(LoginRequiredMixin,UpdateView):
    model = Note
    fields = '__all__'
