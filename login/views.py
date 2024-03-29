from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


# Create your views here.

def user_login(request):
    if request.method=='POST':
        form= AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    
    else:
        form = AuthenticationForm()
    return render(request,'login/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login') #Redirect to the login page

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})
