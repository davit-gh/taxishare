from django.db import models

# Create your models here.
from django.db import models

class MyProfile(models.Model):
    user = models.OneToOneField("auth.User")
    balance = models.FloatField(blank=True, default=0.0)
