from django.db import models


class AboutUs(models.Model):
    image = models.ImageField("Фото о нас", upload_to="about/img/")
    title = models.CharField("Название о нас", max_length=100)
    one_fact = models.CharField("Один факт о нас", max_length=80)
    description = models.TextField("Описание", max_length=1000)
    
    # three pluses about us
    first_plus = models.CharField("Первый плюс", max_length=50)
    first_plus_desc = models.CharField("Описание первого плюса", max_length=200)
    second_plus = models.CharField("Второй плюс", max_length=50)
    second_plus_desc = models.CharField("Описание второго плюса", max_length=200)
    third_plus = models.CharField("Третий плюс", max_length=50)
    third_plus_desc = models.CharField("Описание третьего плюса", max_length=200)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class PartnersAbout(models.Model):
    about = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
    partners_image = models.ImageField("Фото", blank=True)
    

    class Meta:
        verbose_name = "Лого Партнера"
        verbose_name_plural = "Лого партнеров"

    
class AboutAuthor(models.Model):
    image = models.ImageField("Фото", upload_to='about/author/')
    name = models.CharField("Имя", max_length=30)
    bio = models.TextField("Био")

    # social
    facebook = models.CharField("Ссылка на Фейсбук", max_length=100)
    google_link = models.CharField("Ссылка на Гугл почту", max_length=100)
    twitter = models.CharField("Ссылка на Твиттер", max_length=100)
    instagram = models.CharField("Ссылка на Инстаграмм", max_length=100)
    pinteres = models.CharField("Ссылка на Пинтерес", max_length=100)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Наш Автор"
        verbose_name_plural = "Наши Авторы"