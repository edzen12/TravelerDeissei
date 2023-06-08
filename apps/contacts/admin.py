from django.contrib import admin

from .models import Contact, ContactMessage


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['location', 'phone1', 'email1']


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name']