from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class founditem(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)  
    description = models.TextField()  
    date_lost = models.DateField()  
    location = models.CharField(max_length=200) 
    contact_email = models.EmailField()  

    def __str__(self):
        return self.name  
