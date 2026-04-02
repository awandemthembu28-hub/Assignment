from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    """Login page view"""
    if request.method == 'POST':
        # Handle login (basic for now)
        messages.info(request, 'Login functionality will be implemented.')
        return redirect('home')
    
    return render(request, 'accounts/login.html')

def home(request):
    return render(request, 'home.html')
