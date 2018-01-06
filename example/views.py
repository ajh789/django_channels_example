from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# User = get_user_model()

# Create your views here.

#@login_required(login_url='/login/')
def user_list(request):
    users = User.objects.select_related('logged_in_user') # Field logged_in_user in model LoggedInUser
    for user in users:
        if hasattr(user, 'logged_in_user'):
            user.status = 'Online'
            user.is_logged_in = True
        else:
            user.status = 'Offline'
            user.is_logged_in = False
    return render(request, 'user_list.html', {'users': users})

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
@login_required(login_url='/login/')
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
