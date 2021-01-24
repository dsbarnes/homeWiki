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


# This is to create things like Apple, Cheese, Trash Bags, etc
class GroceryListItem(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Once we have the grocery items to select from
# We give what add information about what we bought, as an entry in the DB
# Then we can say, for each model.Grocery with a name == model.GroceryListItem
class Grocery(models.Model):
    item = models.ForeignKey('GroceryListItem', on_delete=models.CASCADE)
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
        return f'{self.name}: ({self.quantity}) {self.item} - {self.date}'
