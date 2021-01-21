from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime


class Finance(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    slug = models.SlugField(unique=True, null=False)

    INCOME = 'I'
    DEBT = 'D'
    EXPENSE = 'E'
    FINANCE_TYPE_OPTIONS = [
        (INCOME, 'Income'),
        (DEBT, 'Debt'),
        (EXPENSE, 'Expense')
    ]

    finance_type = models.CharField(
        max_length=1,
        choices=FINANCE_TYPE_OPTIONS,
    )

    def __str__(self):
        return f'{self.name}: ${self.amount}'

    def save(self, *args, **kwargs):
        # Only give a slug and datetime when the object is initially created
        if not self.id:
            self.slug = slugify(self.name)
            self.date = datetime.now()
        # Need to look more into what is going on with all of this
        super(Finance, self).save(*args, **kwargs)
