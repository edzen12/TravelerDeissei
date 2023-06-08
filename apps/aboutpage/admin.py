from django.contrib import admin

from .models import AboutUs, PartnersAbout, AboutAuthor


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PartnersAbout)
class PartnersAboutAdmin(admin.ModelAdmin):
    list_display = ['about', 'id']

@admin.register(AboutAuthor)
class AboutAuthorAdmin(admin.ModelAdmin):
    list_display = ['name']