from django.shortcuts import render
from django.views.generic import ListView

from .models import Destination

from apps.homepage.models import SettingMain
from apps.blogs.models import Blog

class DestinationListView(ListView):
    model = Destination
    queryset = Destination.objects.all()
    template_name = "destination/destination.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingMain.objects.get(active=True)
        context['blogs'] = Blog.objects.all()[::-1][:2]
        return context 
