from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify


class HomeDocs(models.Model):
    name = models.CharField(max_length=255)
    media = models.FileField()
    details = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=False)

    INSPECTION = 'I'
    PURCHASE = 'P'
    ROOM = 'R'
    DOC_TYPE_CHOICES = [
        (INSPECTION, 'Inspection'),
        (PURCHASE, 'Purchase'),
        (ROOM, 'room'),
    ]

    doc_type = models.CharField(
        max_length=1,
        choices=DOC_TYPE_CHOICES,
    )


    def __str__(self):
        return f'{self.doc_type}: {self.name}'


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        
        super(HomeDocs, self).save(*args, **kwargs)