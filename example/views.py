from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse

# Create your views here.
def user_list(request):
    return render(request, 'user_list.html')

# Log in
def signin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('example:user_list'))
        else:
            print(form.errors)
    return render(request, 'login.html', {'form': form})

# Log out
def signout(request):
    logout(request)
    return redirect(reverse('example:login'))

# Register
def singup(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('example:login'))
        else:
            print(form.errors)
    return render(request, 'signup.html', {'form': form})
