from django.contrib import admin
from .models import SettingMain, SliderMain


@admin.register(SettingMain)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']


@admin.register(SliderMain)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
