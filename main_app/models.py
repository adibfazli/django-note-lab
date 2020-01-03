from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

STATUS = (
    ('U' , 'Urgent'),
    ('A' , 'About time'),
    ('C' , 'chill')
)

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    status = models.CharField(
         max_length=3,
        choices=STATUS,
        default=STATUS[1][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} \n {self.content}'

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'pk': self.id})

class Detail(models.Model):
    sub_note = models.TextField(max_length=500)
    note = models.ForeignKey(Note,on_delete=models.CASCADE)
