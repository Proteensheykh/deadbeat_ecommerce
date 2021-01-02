from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name