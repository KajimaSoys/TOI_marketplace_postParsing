from django.db import models


class Product(models.Model):
    """"This model defines the concept of a Element in our site."""
    title = models.CharField(max_length=120)

    price = models.TextField()
    provider = models.TextField()
    url = models.TextField()
    img = models.TextField()

    def __str__(self):
        return self.title
