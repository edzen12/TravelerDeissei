from django.db import models


class Contact(models.Model):
    # email address
    email1 = models.EmailField("Первый Емаил")
    email2 = models.EmailField("Второй Емаил", blank=True, null=True)
    email3 = models.EmailField("Третий Емаил", blank=True, null=True)

    # phone number
    phone1 = models.CharField("Первый номер", max_length=20)
    phone2 = models.CharField("Второй номер", max_length=20, null=True, blank=True)
    phone3 = models.CharField("Третий номер", max_length=20, null=True, blank=True)

    # address location
    location = models.CharField("Адрес", max_length=100)
    link_google_map = models.CharField("Ссылка адресса из Google Maps", max_length=1000, help_text="<iframe...", null=True, blank=True)

    def __str__(self):
        return self.location
    

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class ContactMessage(models.Model):
    first_name = models.CharField("Имя", max_length=40)
    email = models.EmailField("Емаил")
    comments = models.TextField("Ваше сообщение", max_length=1000)

    def __str__(self):
        return self.first_name
    

    class Meta:
        verbose_name = "Сообщение Контакта"
        verbose_name_plural = "Сообщение из Контактов"
