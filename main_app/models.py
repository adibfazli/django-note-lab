from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.title} \n {self.content}'

class Detail(models.Model):
    sub_note = models.TextField(max_length=500)
    note = models.ForeignKey(Note,on_delete=models.CASCADE)
