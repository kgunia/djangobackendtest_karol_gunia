from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.core import validators
import re
from django.urls import reverse
# Create your models here.
# def validate_telephone(telephone):
#     r = re.compile('^[0-9]+$')
#     if telephone:
#         if len(telephone) > 9 or not r.match(telephone):
#             raise ValidationError("Enter a valid phone number")
#
# def validate_email(email):
#     if email:
#         if not re.search('@',email):
#             raise ValidationError("Enter a valid email adress")

class User(AbstractUser):
    email = models.EmailField(unique = True,
                              help_text = 'The e-mail address must be in the anulujkredyt.pl domain',
                              validators = [validators.RegexValidator(
                                  re.compile('^[\w.@+-]+@anulujkredyt.pl$'), 'Enter a valid email'),
                              ])
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']


class Customer(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    telephone = models.CharField(max_length=9, null=True,help_text = 'No more than 9 digits and no spaces',
                                 validators = [
                                     validators.RegexValidator(re.compile('^[0-9]+$'), 'Enter a valid number'),
                                 ])

    def get_absolute_url(self):
        return reverse('customer-update', kwargs={'pk': self.pk})


    def __str__(self):
        return f"{self.first_name} {self.last_name}"



