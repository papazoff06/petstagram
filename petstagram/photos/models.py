from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_photo_size


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(
        validators=[validate_photo_size],
    )
    description = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10)],
        blank=True, null=True
    )
    location = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    tagged_pets = models.ManyToManyField(Pet, blank=True, related_name='tagged_pets')
    date_of_publication = models.DateTimeField(auto_now=True)
