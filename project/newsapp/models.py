from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=80, help_text='Заголовок новости - 80 символов')
    description = models.TextField(help_text='Детальное описание')
    creation_date = models.DateField(help_text='Дата создания')
    update_date = models.DateField(help_text='Дата обновления')

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Article(models.Model):
    title = models.CharField(
        max_length=80, help_text='Заголовок cтатьи - 80 символов')
    description = models.TextField(help_text='Детальное описание')
    creation_date = models.DateField(help_text='Дата создания')
    update_date = models.DateField(help_text='Дата обновления')
    news= models.ManyToManyField(News)
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"