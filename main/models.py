# Create your models here.
from django.db import models
from functools import partial
from django import forms
from ajax_select.fields import AutoCompleteField
from happenings.models import Event
from happenings.models import Streets
from django.contrib.auth.models import User

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class MyProfile(models.Model):
    user = models.OneToOneField("auth.User")
    balance = models.FloatField(blank=True, default=0.0)
    mobile_number = models.IntegerField(blank=False)
    pin = models.IntegerField(blank=False)
    

class SourceDest(models.Model):
	source = models.ForeignKey(Streets, blank=True, related_name='source_set')
	destination = models.ForeignKey(Streets, blank=True, related_name='destination_set')
	book_date = models.DateField()
        timestamp = models.TimeField()

class Feedback(models.Model):
    event = models.ForeignKey(Event, related_name="event")
    user = models.ForeignKey(User, related_name="usr")
    title = models.CharField(max_length=100, blank=False)
    feedback_desc = models.TextField(blank=False)
    feedback_date = models.DateTimeField(auto_now_add=True, blank=True)

from paypal.standard.ipn.signals import payment_was_successful
from main.views import set_user_balance
from main.views import get_user_balance

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    # You need to check 'payment_status' of the IPN

    if ipn_obj.payment_status == "Completed":
        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom:
        	amountAMD, user = ipn_obj.custom.split(',')
        	u = User.objects.get(username=user)
        	balance = get_user_balance(u)
        	new_balance = balance + int(amountAMD)
        	set_user_balance(u, new_balance)
    
        

payment_was_successful.connect(show_me_the_money)