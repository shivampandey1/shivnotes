from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField(null=True, blank=True) #body of note can not exist or be blank
    updated = models.DateTimeField(auto_now=True) #save time of last update
    created = models.DateTimeField(auto_now_add=True) #save time of creation

    def __str__(self):
        return self.body[0:50] #return first 50 characters of the note