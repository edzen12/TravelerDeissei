from django.db import models


class GuideProffesion(models.Model):
    title = models.CharField("Название Профессии", max_length=60)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Профессия гида"
        verbose_name_plural = "Профессия гидов"


class Guide(models.Model):
    name = models.CharField("Имя", max_length=30)
    proffesion = models.ForeignKey(GuideProffesion, on_delete=models.SET_DEFAULT, default=None, verbose_name="Профессия")
    bio = models.CharField("Коротко о себе", max_length=600)

    # social
    facebook = models.CharField("Ссылка на фейсбук", max_length=200, blank=True, null=True)
    twitter = models.CharField("Ссылка на Твиттер", max_length=200, blank=True, null=True)
    instagram = models.CharField("Ссылка на Инстаграмм", max_length=200, blank=True, null=True)
    youtube = models.CharField("Ссылка на Ютуб", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Гид"
        verbose_name_plural = "Гиды"