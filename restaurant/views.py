from django.shortcuts import render, redirect
from .models import MenuItem, Category, Booking, ContactMessage
from django.contrib import messages

def home(request):
    featured_items = MenuItem.objects.filter(is_available=True)[:3]
    return render(request, 'restaurant/home.html', {'featured_items': featured_items})

def menu(request):
    categories = Category.objects.all()
    return render(request, 'restaurant/menu.html', {'categories': categories})

def book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        message = request.POST.get('message')
        
        Booking.objects.create(
            name=name, email=email, phone=phone,
            date=date, time=time, number_of_guests=guests,
            message=message
        )
        messages.success(request, 'Your table has been booked successfully!')
        return redirect('home')
        
    return render(request, 'restaurant/book.html')

def about(request):
    return render(request, 'restaurant/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('msg')
        
        ContactMessage.objects.create(
            name=name, email=email,
            subject=subject, message=message
        )
        messages.success(request, 'Thank you for your message. We will get back to you soon!')
        return redirect('contact')
        
    return render(request, 'restaurant/contact.html')

