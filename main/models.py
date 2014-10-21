# Create your models here.
from django.db import models
from functools import partial
from django import forms
from ajax_select.fields import AutoCompleteField

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class MyProfile(models.Model):
    user = models.OneToOneField("auth.User")
    balance = models.FloatField(blank=True, default=0.0)
    mobile_number = models.IntegerField(blank=False)
    pin = models.IntegerField(blank=False)
    


class Streets(models.Model):
	name_en = models.CharField(max_length=100)
	name_hy = models.CharField(max_length=100)
	
	def __unicode__(self):
	        return self.name_en

class SourceDest(models.Model):
	source = models.ForeignKey(Streets, blank=True, related_name='source_set')
	destination = models.ForeignKey(Streets, blank=True, related_name='destination_set')
	book_date = models.DateField()
        timestamp = models.TimeField()


