from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError("Please enter numeric value.")


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, validators=[validate_phone_number])
    address = models.TextField()

    def __str__(self):
        return self.name
