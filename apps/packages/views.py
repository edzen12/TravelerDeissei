from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from apps.blogs.models import Blog
from apps.contacts.models import Contact
from apps.destinations.models import Destination
from apps.gallery.models import Gallery
from apps.homepage.models import SettingMain
from apps.packages.forms import CountryForm

from .models import Country, Package
from .serializers import PackageSerializer


class PackageDetailVew(DetailView):
    model = Package
    slug_field = "slug"
    template_name = "package/package-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingMain.objects.get(active=True)
        context['blogs'] = Blog.objects.all()[::-1][:2]
        context['images'] = Gallery.objects.all()[2:8]
        context['contacts'] = Contact.objects.get(id=1)
        return context 


class PackageListView(ListView):
    model = Package
    queryset = model.objects.filter(activate_promo=True)
    template_name = "package/package-offer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingMain.objects.get(active=True)
        context['blogs'] = Blog.objects.all()[::-1][:2]
        context['images'] = Gallery.objects.all()[2:8]
        context['contacts'] = Contact.objects.get(id=1)
        context['countries'] = Country.objects.all()
        return context 


class PackageNoPromoListView(ListView):
    model = Package
    queryset = model.objects.all()
    template_name = "package/package.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingMain.objects.get(active=True)
        context['blogs'] = Blog.objects.all()[::-1][:2]
        context['images'] = Gallery.objects.all()[2:8]
        context['contacts'] = Contact.objects.get(id=1)
        context['countries'] = Country.objects.all()
        context['destinations'] = Destination.objects.all()
        
        return context 


class PackageViewSet(ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

def package_list(request):
    country_filter = request.GET['country']
    min_price_filter = request.GET.get('min_price')
    max_price_filter = request.GET.get('max_price')
    destination = request.GET.get('destination')

    countries = Country.objects.all()
    destinations = Destination.objects.all()

    packages = Package.objects.all()
    setting = SettingMain.objects.get(active=True)
    blogs = Blog.objects.all()[::-1][:2]
    images = Gallery.objects.all()[2:8]
    contacts = Contact.objects.get(id=1)


    if country_filter:
        packages = packages.filter(country__title=country_filter)

    if min_price_filter and max_price_filter:
        packages = packages.filter(price_per_person__gte=min_price_filter, price_per_person__lte=max_price_filter)

    if destination:
        packages = packages.filter(destination__title=destination)

    return render(request, 'package/package.html', locals())
