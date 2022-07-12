from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.forms import EmailField

class Assignment(models.Model):
    date = models.DateTimeField(blank=True, default="YYYY-MM-DD HH:MM:SS")
    company = models.CharField(max_length=200, blank=True, default="None")
    language = models.CharField(max_length=200, blank=True, default="None")
    patient = models.CharField(max_length=200, blank=True, default="None")
    po_num = models.BigIntegerField(blank=True, default=00000)
    type = models.CharField(max_length=200, blank=True, default="None")
    hours = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)
    hourly_rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0)
    miles = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)
    mileage_rate = models.DecimalField(max_digits=3, decimal_places=2, blank=True, default=0)
    address = models.CharField(max_length=200, blank=True, default="None")
    flat_rate = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)
    parking = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)
    interpreter = models.CharField(max_length=200, blank=True, default="None")
    is_invoiced = models.BooleanField(default=1, blank=True)
    is_paid = models.BooleanField(default=1, blank=True)
    offered_to = models.TextField(blank=True)
    interpreter_payment = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)
    completed = models.BooleanField(default=0, blank=True)

class Company(models.Model):
    name = models.CharField(max_length=200)
