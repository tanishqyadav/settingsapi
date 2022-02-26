
from typing_extensions import Required
from django.db import models

from datetime import datetime
from django.forms import HiddenInput

from matplotlib import widgets

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    is_active = models.BooleanField(default=True)




