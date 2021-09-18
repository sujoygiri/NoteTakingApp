from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    note_sub = models.CharField(max_length=800)
    note_detail = models.TextField(null=True,blank=True)
    creating_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.note_sub