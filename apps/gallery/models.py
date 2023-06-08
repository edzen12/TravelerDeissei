from django.db import models


class Gallery(models.Model):
    title = models.CharField("Название", max_length=10, blank=True, null=True)
    image = models.ImageField("Картинка", upload_to="gallery/")

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"
