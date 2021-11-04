from django.db import models
from django.core.exceptions import ValidationError
from .utils import make_code

# Validating error message
def validate_empty_first_name(value):
    if not value == "":
        return value
    else:
        raise ValidationError("The first name cannot be empty!")

# Create your models here.
class UserList(models.Model):
    id = models.CharField(max_length=16, blank=True)
    email = models.EmailField(max_length=254, primary_key=True)
    first_name = models.CharField(max_length=15, validators=[validate_empty_first_name])
    last_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=20,default='+6282637778888')
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.id == "":
            self.id = make_code()

        return super(UserList, self).save(*args, **kwargs)
