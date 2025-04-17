from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
#Create your models here.

class User(AbstractUser):  
    #phone_number = models.CharField(max_length=20 , unique=True)
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = []  # No username required
    username = models.CharField(max_length=20)
    USERNAME_FIELD = 'email'  # Set email as the primary field for authentication
    group = None
    user_permissions = None
    
    objects = UserManager()

    def __str__(self):
        return self.email


class Founditem(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)    
    name = models.CharField(max_length=200)  
    description = models.TextField()  
    date_found = models.DateField()  
    location = models.CharField(max_length=200) 
    contact_email = models.EmailField()  

    def __str__(self):
        return self.name 
    



class LostItem(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=255)  
    description = models.TextField()  
    location_lost = models.CharField(max_length=255)  
    date_lost = models.DateField()  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='lost')  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.title} ({self.status})"


class FoundItemRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='found_item_requests')
    found_item = models.ForeignKey(Founditem, on_delete=models.CASCADE, related_name='requests')
    message = models.TextField(blank=True, null=True)  #message to explain ownership
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.requester.email} for {self.found_item.title} - {self.status}"
