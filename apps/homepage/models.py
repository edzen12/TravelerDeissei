from django.db import models
from django.core.exceptions import ValidationError


class SettingMain(models.Model):
    title = models.CharField("Название", max_length=30)
    number = models.CharField("Номер", max_length=20)
    description = models.TextField("Описание Сайта", max_length=700)
    icon = models.ImageField("Иконка", upload_to='home/icon/')
    logo = models.ImageField("Логотип", upload_to='home/logo/')

    # video
    link_video = models.CharField("Ссылка на Видео", max_length=100)

    # socials
    facebook = models.CharField("Ссылка на Фейсбук", max_length=100)
    twitter = models.CharField("Ссылка на Твиттер", max_length=100)
    youtube = models.CharField("Ссылка на Ютуб", max_length=100)
    instagram = models.CharField("Ссылка на Инстарам", max_length=100)
    linkedin = models.CharField("Ссылка на Линкедин", max_length=100)

    active = models.BooleanField("Активировать", default=False)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'


class SliderMain(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Краткое описание", max_length=500)
    banner = models.ImageField("Баннер", upload_to='home/banner/')

    active = models.BooleanField("Активировать", default=False)

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Основной Баннер'
        verbose_name_plural = 'Основные Баннеры'
