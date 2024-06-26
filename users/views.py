from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout



def registeruser(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
             form.save()
             username=form.cleaned_data.get('username') 
             messages.success(request,f'Account created for {username}!')
             return redirect('login')        
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})
    
def logoutUser(request):
    logout(request)
    return redirect('shipping-home')    

# Create your views here.
