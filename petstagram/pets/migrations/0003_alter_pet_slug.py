# Generated by Django 5.1.2 on 2024-11-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_rename_pets_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
