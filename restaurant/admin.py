from django.contrib import admin
from .models import Category, MenuItem, Booking, ContactMessage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'number_of_guests', 'created_at')
    list_filter = ('date', 'created_at')
    search_fields = ('name', 'email', 'phone')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject')

