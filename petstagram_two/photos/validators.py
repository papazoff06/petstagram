from django.core.exceptions import ValidationError


def photo_size_validator(value):
    if value.size > 5242880:
        raise ValidationError('The maximum file size that can be uploaded is 5MB')