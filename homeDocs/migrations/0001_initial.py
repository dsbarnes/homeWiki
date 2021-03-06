# Generated by Django 3.1.4 on 2021-01-24 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('media', models.FileField(upload_to='')),
                ('details', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('doc_type', models.CharField(choices=[('I', 'Inspection'), ('P', 'Purchase'), ('R', 'room')], max_length=1)),
            ],
        ),
    ]
