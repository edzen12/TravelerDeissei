import random

from django.db import models

from apps.packages.models import Package
from apps.cartitems.models import CartItem


class Booking(models.Model):
    booking_id_save = ''

    def four_num_card(self, card):
        return card[::-1][:4]
    
    def booking_id_generator(self):
        a = ''
        for i in range(6):
            a+=str(random.randint(1, 9))
        return a

    # your details
    first_name = models.CharField("Имя", max_length=60)
    last_name = models.CharField("Фамилия", max_length=60)
    email = models.EmailField("Емаил")
    confirm_email = models.EmailField("Подтверджение Емаила")
    phone = models.CharField("Номер Телефона", max_length=20)


    # payment information
    name_on_card = models.CharField("Имя на карте", max_length=40)
    card_number = models.CharField("Номер карты", max_length=16)
    expiration_date = models.CharField("Месяц / Год", max_length=5)
    year = models.CharField("Год получения", max_length=4)
    ccv = models.CharField("CCV", max_length=3)

    package = models.ForeignKey(Package, on_delete=models.CASCADE, blank=True, null=True)
    
    # main models
    cart_item = models.ManyToManyField(
        CartItem,
        related_name='cart_item_booking',
        blank=True,
    )

    @property
    def num_card(self):
        a = self.four_num_card(self.card_number)
        return a[::-1]
    
    def first_num_card(self):
        return self.card_number[0]