from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        # Get the username and password from the request
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        # If the user is not None, log them in
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Error logging in - please try again...'))
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})
    

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username'] # Get the username from the form
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password) # Authenticate the user
            login(request, user)
            messages.success(request, ('You have been registered!'))
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated == False:
        messages.success(request, ('Please login to view records...'))
        return redirect('home')
    record = Record.objects.get(id=pk)
    return render(request, 'record.html', {'record':record})

def delete_record(request, pk):
    if request.user.is_authenticated == False:
        messages.success(request, ('Please login to delete records...'))
        return redirect('home')
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, ('Record has been deleted...'))
    return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)

    if request.user.is_authenticated == False:
        messages.success(request, ('Please login to add records...'))
        return redirect('home')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, ('Record has been added...'))
            return redirect('home')
        return redirect('home')
    else:
        return render(request, 'add_record.html', {'form':form})
    

def update_record(request, pk):
    if request.user.is_authenticated == False:
        messages.success(request, ('Please login to update records...'))
        return redirect('home')
    record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=record)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, ('Record has been updated...'))
            return redirect('home')
    else:
        return render(request, 'update_record.html', {'form':form})