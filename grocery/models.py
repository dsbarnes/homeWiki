from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify


# Create your models here.
class Recipt(models.Model):
    name = models.CharField(max_length=255)
    reciept = models.ImageField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Recipt, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Grocery(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Grocery, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
