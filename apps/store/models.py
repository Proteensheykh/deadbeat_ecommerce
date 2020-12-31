from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name