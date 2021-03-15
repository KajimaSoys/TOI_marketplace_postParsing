from django.db import models


class Product(models.Model):
    """This model defines the concept of a Element in our site."""
    title = models.CharField(max_length=120)

    price = models.TextField()
    provider = models.TextField()
    url = models.TextField()
    img = models.TextField()

    def __str__(self):
        return self.title


class Stats(models.Model):
    """This model defines stats in our site."""
    querystring = models.CharField("Запрос", max_length=120, unique=True)
    amount = models.IntegerField("Количество", default=0)

    def __str__(self):
        return self.querystring

    class Meta:
        verbose_name = "Поисковый запрос"
        verbose_name_plural = "Статистика поисковых запросов"
        ordering = ("querystring", "amount")