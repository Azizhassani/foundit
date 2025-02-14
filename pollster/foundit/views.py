from django.shortcuts import render
from .models import founditem

# Create your views here.

def index(request):
    items = founditem.objects.all()
    return render(request,'foundit/index.html',{'items':items})