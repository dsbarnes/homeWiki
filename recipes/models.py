from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)
    directions = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Only give a slug when the recipe is initially created
        if not self.id:
            self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)
