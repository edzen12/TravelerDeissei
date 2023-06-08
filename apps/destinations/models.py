from django.db import models


class Destination(models.Model):
    def raiting_сalc(self, raiting:int):
        if raiting == 0:
            return 0
        percent = {20: 100, 25: 80, 33: 60, 50: 40, 100: 20, 0: 0}
        func = 100 // raiting
        if func in percent.keys():
            return percent[func]

    country = models.CharField("Страна", max_length=40)
    title = models.CharField("Название", max_length=60)
    description = models.TextField("Описание")

    raiting_num = models.IntegerField("Рейтинг", help_text="От 1 до 5", default=0)
    
    @property
    def raiting(self):
        return self.raiting_сalc(int(self.raiting_num))

    image = models.ImageField("Картинка для постера", upload_to="destination/")

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"
