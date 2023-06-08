from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView
from django.contrib import messages

from apps.packages.models import Package
from apps.cartitems.models import CartItem

from .models import Booking

from apps.homepage.models import SettingMain
from apps.blogs.models import Blog
from apps.gallery.models import Gallery
from apps.contacts.models import Contact


class BookingPackage(DetailView):
    model = Package
    slug_field = "slug"
    template_name = "booking/booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


def bookingPackage(request):
    carts = CartItem.objects.filter(user=request.user, status='NA')

    total = 0

    for cart_item in carts:
        if cart_item.status == 'NA':
            total+=cart_item.total_price

    # settings main
    setting = SettingMain.objects.get(active=True)
    blogs = Blog.objects.all()[::-1][:2]
    images = Gallery.objects.all()[2:8]
    contacts = Contact.objects.get(id=1)
    return render(request, "booking/booking.html", locals())


def booking_add_package(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        confirm_email = request.POST['confirm_email'] 
        phone = request.POST['phone'] 
        name_on_card = request.POST['name_on_card'] 
        card_number = request.POST['card_number'] 
        expiration_date = request.POST['expiration_date'] 
        year = request.POST['year'] 
        ccv = request.POST['ccv'] 
        cart_item = CartItem.objects.filter(user=request.user, status='NA')

        instance = Booking.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            confirm_email=confirm_email,
            phone=phone,
            name_on_card=name_on_card,
            card_number=card_number,
            expiration_date=expiration_date,
            year=year,
            ccv=ccv,
        )
        instance.cart_item.set(cart_item)
        return redirect('finish_booking', instance.id)


# def booking_add_package(request, pk):
#     if request.method == 'POST':
#         print(True)
#         form = BookingForm(request.POST)
#         cart_item = CartItem.objects.get(id=pk)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.cart_item = cart_item
#             form.save()
#             return redirect('finish_booking', cart_item.id)


     

def booking_finish(request, pk):
    booking = Booking.objects.get(id=pk)

    total = 0

    for cart_ite in booking.cart_item.all():
        if cart_ite.status == 'NA':
            total+=cart_ite.total_price
            cart_ite.status = 'FN'
            cart_ite.save()
            print(cart_ite.status)
    
    
    
    # settings
    setting = SettingMain.objects.get(active=True)
    blogs = Blog.objects.all()[::-1][:2]
    images = Gallery.objects.all()[2:8]
    contacts = Contact.objects.get(id=1)
    return render(request, 'booking/confirmation.html', locals())
