from django.shortcuts import render
from django.views.generic.base import View

from .models import AboutUs, PartnersAbout

from apps.contacts.models import Contact
from apps.gallery.models import Gallery
from apps.blogs.models import Blog
from apps.homepage.models import SettingMain

class AboutView(View):
    def get(self, request):
        aboutus = AboutUs.objects.get(id=1)
        photo_partners = PartnersAbout.objects.filter(about=aboutus.id)

        # footer-contacts
        contacts = Contact.objects.get(id=1)
        images = Gallery.objects.all()[2:8]
        blogs = Blog.objects.all()[::-1][:2]

        # main settings
        setting = SettingMain.objects.get(active=True)
        return render(request, 'about/about.html', locals())

