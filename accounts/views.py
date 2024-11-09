from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib import messages
from django.urls import reverse_lazy
from accounts.forms import SignUpForm


def entrance(request):
    return render(request, 'accounts/index.html')

class Login(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('index')

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'{user.username} присоединился к нам!')
            return redirect('/events')
        
    else:
        form = SignUpForm()
    return render(request, 'accounts/registration.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/')