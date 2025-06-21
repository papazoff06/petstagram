from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_two.pets.models import Pet
from petstagram_two.photos.validators import photo_size_validator

UserModel = get_user_model()
# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(upload_to='images', validators=[photo_size_validator])
    description = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10)],
        null=True,
        blank=True,
    )
    location = models.CharField(max_length=30, null=True, blank=True)
    tagged_pets = models.ManyToManyField(to=Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)