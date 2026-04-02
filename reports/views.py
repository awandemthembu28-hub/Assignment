from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def home(request):
    """Home page view"""
    return render(request, 'home.html')

def report_form(request):
    """Report issue form view"""
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'report':
            # Handle report submission
            messages.success(request, '✅ Your report has been submitted successfully! Reference: WW-2024-004')
        elif form_type == 'pickup':
            # Handle pickup request
            messages.success(request, '✅ Your pickup request has been submitted! Reference: PU-2024-001')
        
        return redirect('report_form')
    
    return render(request, 'reports/report_form.html')

def pickup_request(request):
    """Pickup request view - redirects to report form with pickup tab"""
    return render(request, 'reports/report_form.html', {'active_tab': 'pickup'})

def status(request):
    """Status tracking view"""
    return render(request, 'reports//templates/status.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
