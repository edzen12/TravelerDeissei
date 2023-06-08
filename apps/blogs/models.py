from django.db import models
from django.urls import reverse

class AuthorBlog(models.Model):
    photo = models.ImageField("Фото", upload_to="author/")
    name = models.CharField("Имя", max_length=30)
    bio = models.CharField("Немного о себе", max_length=200)

    # social
    facebook = models.CharField("Ссылка на Фейсбук", max_length=100, blank=True, null=True)
    google = models.CharField("Ссылка на Гугл Почту", max_length=100, blank=True, null=True)
    twitter = models.CharField("Ссылка на Гугл Почту", max_length=100, blank=True, null=True)
    instagram = models.CharField("Ссылка на Гугл Почту", max_length=100, blank=True, null=True)
    pinteres = models.CharField("Ссылка на Гугл Почту", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class CategoryBlog(models.Model):
    title = models.CharField("Название категории", max_length=50)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Blog(models.Model):
    image = models.ImageField("Фото", upload_to="blogs/")
    backgroung = models.ImageField("Фото для заднего фона", upload_to="blogs/back/", null=True, blank=True)
    title = models.CharField("Название", max_length=50)
    create_add = models.DateField("Время добавление", auto_now_add=True)

    description = models.TextField("Описание")
    my_comment = models.TextField("Мои комментарии", blank=True, null=True)
    category = models.ManyToManyField(CategoryBlog, verbose_name="Категории")
    author = models.ForeignKey(AuthorBlog, on_delete=models.CASCADE, verbose_name="Автор")

    slug = models.SlugField("Ссылка", unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
    


    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"


class ReviewBlog(models.Model):
    name = models.CharField("Имя", max_length=30)
    email = models.EmailField("Емаил", max_length=254)
    message = models.TextField("Отвыз", max_length=500)
    create_add = models.DateField("Добавление", auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Блог", related_name='comments_blog')

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"





