from django.shortcuts import render,redirect
from .models import founditem
from .forms import foundForm ,registerform
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    items = founditem.objects.all()
    return render(request,'foundit/index.html',{'items':items})

@login_required
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
            return redirect('lost_items_list')  
    else:
        form = registerform()
    
    return render(request, 'foundit/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) 
            return redirect('lost_items_list')  
    else:
        form = AuthenticationForm()
    
    return render(request, 'foundit/login.html', {'form': form})

def user_logout(request):
    logout(request)  
    return redirect('lost_items_list')  



