# Generated by Django 3.1.4 on 2021-01-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateField()),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('reciept', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
            ],
        ),
    ]
