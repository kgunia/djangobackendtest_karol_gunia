from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.core import validators
import re
from django.urls import reverse



class User(AbstractUser):
    username = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique = True, blank=False,
                              help_text = 'The e-mail address must be in the anulujkredyt.pl domain',
                              validators = [validators.RegexValidator(
                                  re.compile('^[\w.@+-]+@anulujkredyt.pl$'), 'Enter a valid email'),
                              ])
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email

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

CARS = (
    (1, 'Red'),
    (2, 'Green'),
    (3, 'Blue')
)
class Car(models.Model):
    name = models.IntegerField(choices=CARS)


    def __str__(self):
        return self.get_name_display()

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer} - {self.product}"

    def get_absolute_url(self):
        return reverse('purchase-list')