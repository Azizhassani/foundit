from django.shortcuts import render,redirect
from .models import founditem
from .forms import foundForm ,registerform
from django.contrib.auth import login

# Create your views here.

def index(request):
    items = founditem.objects.all()
    return render(request,'foundit/index.html',{'items':items})

def add_lost_item(request):
    if request.method == "POST":
        form = foundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lost_items_list')
    else:
        form = foundForm()
    return render(request,'foundit/add_lost_item.html',{'form':form})

def register(request):
    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])  # Hash
            user.save()  
            login(request, user)  
            return redirect('home')  
    else:
        form = registerform()
    
    return render(request, 'foundit/register.html', {'form': form})

