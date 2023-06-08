from django.contrib import admin

from .models import Guide, GuideProffesion

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ['name', 'proffesion']


@admin.register(GuideProffesion)
class GuideProffesionAdmin(admin.ModelAdmin):
    list_display = ['title']

