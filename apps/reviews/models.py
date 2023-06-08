from django.db import models


class Review(models.Model):
    def raiting_сalc(self, raiting:int):
        if raiting == 0:
            return 0
        percent = {20: 100, 25: 80, 33: 60, 50: 40, 100: 20, 0: 0}
        func = 100 // raiting
        if func in percent.keys():
            return percent[func]
    
    who_list = [
        ("Путешественник", "Путешественник"),
        ("Турист", "Турист"),
    ]

    name = models.CharField("Имя", max_length=30)
    photo = models.ImageField("Фото", upload_to='photo_review/')
    who = models.CharField("Кто вы", max_length=14, choices=who_list)
    raiting_num = models.IntegerField("Рейтинг", help_text="От 1 до 5", default=0)

    @property
    def raiting(self):
        return self.raiting_сalc(int(self.raiting_num))
    
    message_review = models.TextField("Отвыз", max_length=500)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Отзыв клиента"
        verbose_name_plural = "Отзывы клиентов"