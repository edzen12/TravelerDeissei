from django.db import models
from django.core.validators import MaxLengthValidator

from apps.destinations.models import Destination

from django.urls import reverse


class Country(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Название",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Страну"
        verbose_name_plural = "Страны"


class CategoryPackage(models.Model):
    title = models.CharField("Название категории", max_length=100)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Категория Пакет"
        verbose_name_plural = "Категория Пакетов"


class IncludePackage(models.Model):
    title = models.CharField("Название включении проездки", max_length=100)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Включения в Пакет"
        verbose_name_plural = "Включения в Пакеты"


class ExcludePackage(models.Model):
    title = models.CharField("Название исключении проездки", max_length=100)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Исключения в Пакет"
        verbose_name_plural = "Исключения в Пакеты"


class ItineraryPackage(models.Model):
    title = models.CharField("Марштрут", max_length=100, help_text="DAY 1 - ....")

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Маршрут Пакет"
        verbose_name_plural = "Маршрут Пакетов"


class Package(models.Model):
    def price_activate_promotion(self, price, percent):
        return price - ((price/100)*percent)
    
    def raiting_сalc(self, raiting:int):
        if raiting == 0:
            return 0
        percent = {20: 100, 25: 80, 33: 60, 50: 40, 100: 20, 0: 0}
        func = 100 // raiting
        if func in percent.keys():
            return percent[func]

    title = models.CharField("Название", max_length=400)
    raiting_num = models.IntegerField('Рейтинг', default=0, help_text="Оценка от 1 до 5")
    price_per_person = models.PositiveSmallIntegerField("Цена на одного человека")

    @property
    def raiting(self):
        return self.raiting_сalc(int(self.raiting_num))
    
    days = models.IntegerField("Длительность дней")
    nights = models.IntegerField("Длительность ночей")

    max_person = models.IntegerField("Максимальное количество людей")

    percent = models.PositiveSmallIntegerField("Процент для действии акции", blank=True, null=True)
    @property
    def price_promo(self):
        return self.price_activate_promotion(self.price_per_person, self.percent)
    activate_promo = models.BooleanField("Активация акции", default=False)

    category = models.ForeignKey(CategoryPackage, on_delete=models.SET_DEFAULT, default=None, verbose_name="Категории")
    travel_country = models.CharField("Страна поездки", max_length=50, null=True, blank=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Пункт названачения'
    )

    image = models.ImageField("Фото", upload_to='package/')
    overview = models.TextField("Обзор", max_length=1000)

    include = models.ManyToManyField(IncludePackage, verbose_name="Включения в поездке")
    exclude = models.ManyToManyField(ExcludePackage, verbose_name="Исключения в поездке")

    itinerary = models.ManyToManyField(ItineraryPackage, verbose_name="Маршрут")
    itinerary_desc = models.TextField("Описание Маршрута", max_length=300)

    slug = models.SlugField("Ссылка", unique=True)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("package_detail", kwargs={"slug": self.slug})
    
    
    def booking_package(self):
        return reverse("package_booking", kwargs={"slug": self.slug})


    class Meta:
        verbose_name = "Пакет"
        verbose_name_plural = "Пакеты"
