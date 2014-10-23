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


from paypal.standard.ipn.signals import payment_was_successful
from django.contrib.auth.models import User
from main.views import set_user_balance
from main.views import get_user_balance

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    # You need to check 'payment_status' of the IPN

    if ipn_obj.payment_status == "Completed":
        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom:
        	amountAMD = ipn_obj.custom
        	u = User.objects.filter(username=request.user)[0]
        	balance = get_user_balance(u)
        	new_balance = balance + int(amountAMD)
        	set_user_balance(u, new_balance)
            
 
        

payment_was_successful.connect(show_me_the_money)