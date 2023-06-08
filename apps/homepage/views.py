from django.shortcuts import render
from django.views import generic

from .models import SettingMain, SliderMain
from apps.destinations.models import Destination
from apps.packages.models import Package

from apps.gallery.models import Gallery

from apps.blogs.models import Blog
from apps.reviews.models import Review
from apps.contacts.models import Contact

class HomePageView(generic.View):
    def get(self, request):
        # main settings
        setting = SettingMain.objects.get(active=True)
        sliders = SliderMain.objects.filter(active=True).order_by('id')[:2]

        # destination
        destinations = Destination.objects.all()[:3]

        # package
        packages = Package.objects.all()[:3]
        packages_promo = Package.objects.filter(activate_promo=True)[:2]

        # images-gallery
        first_image_for_homepage = Gallery.objects.get(id=9)
        second_image_for_homepage = Gallery.objects.get(id=10)
        third_image_for_homepage = Gallery.objects.get(id=11)
        fourth_image_for_homepage = Gallery.objects.get(id=12)
        fifth_image_for_homepage = Gallery.objects.get(id=13)

        # blogs 
        blogs = Blog.objects.all()[::-1][:2]

        # review-clients
        reviews = Review.objects.all()[:4]

        # footer-contacts
        contacts = Contact.objects.get(id=1)
        images = Gallery.objects.all()[2:8]
        
        return render(request, 'home/index.html', locals())


class SearchView(generic.View):
    def get(self, request):
        if 's' in request.GET:
            key = request.GET.get('s')
            destinations = Destination.objects.filter(title__icontains=key)
            blogs_search = Blog.objects.filter(title__icontains=key)
            packages_search = Package.objects.filter(title__icontains=key)

            # main settings
            setting = SettingMain.objects.get(active=True)

            # footer-contacts
            contacts = Contact.objects.get(id=1)
            images = Gallery.objects.all()[2:8]
            blogs = Blog.objects.all()[::-1][:2]

            return render(request, 'searchs/search-page.html', locals())