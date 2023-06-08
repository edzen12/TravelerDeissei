from django.shortcuts import render, redirect
from django.views.generic.base import View


from .models import Contact
from .forms import ContactMessageForm

from apps.blogs.models import Blog
from apps.homepage.models import SettingMain
from apps.gallery.models import Gallery

class ContactDetailView(View):
    def get(self, request):
        contact = Contact.objects.get(id=1)
        setting = SettingMain.objects.get(active=True)
        blogs = Blog.objects.all()[::-1][:2]
        
        # footer
        images = Gallery.objects.all()[2:8]
        contacts = Contact.objects.get(id=1)
        return render(request, 'contact/contact.html', locals())


class AddMessageContact(View):
    def post(self, requets):
        form = ContactMessageForm(requets.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return redirect("/")