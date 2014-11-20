# Create your models here.
from django.db import models
from functools import partial
from django import forms
from ajax_select.fields import AutoCompleteField
from happenings.models import Event
from happenings.models import Streets
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class MyProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    balance = models.FloatField(blank=True, default=0)
    mobile_number = models.CharField(_("Mobile Number"), max_length=20, blank=False)
    pin = models.CharField(_("Pin"), blank=False, max_length=10)
    

class SourceDest(models.Model):
	source = models.ForeignKey(Streets, blank=True, related_name='source_set')
	destination = models.ForeignKey(Streets, blank=True, related_name='destination_set')
	book_date = models.DateField()
        timestamp = models.TimeField()

class Feedback(models.Model):
    event = models.ForeignKey(Event, related_name="event")
    user = models.ForeignKey(User, related_name="usr")
    title = models.CharField(_("Title"), max_length=100, blank=False)
    feedback_desc = models.TextField(_("Feedback Text"), blank=False)
    feedback_date = models.DateTimeField(auto_now_add=True, blank=True)


class Contactus(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=False)
    email = models.EmailField(blank=False)
    title = models.CharField(_("Title"), max_length=100, blank=False)
    description = models.TextField(_("Description"), blank=False)
    message_date = models.DateTimeField(auto_now_add=True, blank=True)

from paypal.standard.ipn.signals import payment_was_successful

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    # You need to check 'payment_status' of the IPN

    if ipn_obj.payment_status == "Completed":
        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom:
        	amountAMD, user = ipn_obj.custom.split(',')
        	u = User.objects.get(username=user)
           	balance = u.profile.balance
           	new_balance = balance + int(amountAMD)
           	u.profile.balance = new_balance
           	u.profile.save()
        

payment_was_successful.connect(show_me_the_money)
