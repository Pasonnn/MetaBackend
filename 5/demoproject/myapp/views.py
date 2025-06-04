from django.shortcuts import render
from .forms import BookingForm
from .models import Employee, Menu
# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    return render(request, 'booking.html', {'form': form})

def employees(request):
    return render(request, 'employees.html')

def drinks(request):
    return render(request, 'drinks.html')

def form_view(request):
    return render(request, 'form.html')