from django.shortcuts import render
from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from ajax_select.fields import AutoCompleteField
from main.forms import StreetsForm
from django.http import HttpResponseRedirect
from twilio.rest import TwilioRestClient
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import MyProfile

# Create your views here.
class SearchForm(forms.Form):

    q = AutoCompleteField(
            'street',
            required=True,
            help_text="Autocomplete will suggest clichs about cats, but you can enter anything you like.",
            label="Favorite Street",
            attrs={'size': 100}
            )


def search_form(request):

    dd = {}
    if 'q' in request.GET:
        dd['entered'] = request.GET.get('q')
    initial = {'q': "\"This is an initial value,\" said O'Leary."}
    form = SearchForm(initial=initial)
    dd['form'] = form
    return render_to_response('search_form.html', dd, context_instance=RequestContext(request))

import random
def _get_pin(length=5):
    """ Return a numeric PIN with length digits """
    return random.sample(range(10**(length-1), 10**length), 1)[0]


def _verify_pin(request, mobile_number, pin):
    """ Verify a PIN is correct """
    return pin == request.session.get('pin')


def ajax_send_pin(request):
    """ Sends SMS PIN to the specified number """
    if request.POST:
	    mobile_number = request.POST.get('mobile_number', "")
	    if not mobile_number:
		return HttpResponse("No mobile number", mimetype='text/plain', status=403)

	    pin = _get_pin()

	    # store the PIN in the cache for later verification.
	    request.session['pin'] = (mobile_number, pin) # valid for 24 hrs

	    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	    message = client.messages.create(
		                body="%s" % pin,
		                to=mobile_number,
		                from_=settings.TWILIO_FROM_NUMBER,
		            )
	    return HttpResponse("Message %s sent, stored pin %s" % (message.sid, pin), mimetype='text/plain', status=200)

    else:
   	    return render(request, 'temp.html')

def set_user_balance(u, new_balance):
    b = MyProfile.objects.filter(user=u)[0]
    b.balance = new_balance
    b.save()

def get_user_balance(u):
    return MyProfile.objects.filter(user=u)[0].balance

import stripe
import pdb
import json
def process_token(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY
	u = User.objects.filter(username=request.user)[0]
	# Get the credit card details submitted by the form
	#pdb.set_trace()	
	token = request.POST['token[id]']

	# Create the charge on Stripe's servers - this will charge the user's card
	try:
	  charge = stripe.Charge.create(
	      amount=2000, # amount in cents, again
	      currency="usd",
	      card=token,
	      description="payinguser@example.com"
	  )
	  amd = float(2000) * 4.11
	  balance = get_user_balance(u)
	  new_balance = balance + amd
	  set_user_balance(u, new_balance)
	  return HttpResponse(json.dumps({'new_balance': str(new_balance)}), mimetype = 'application/json')
	except stripe.CardError, e:
	  # The card has been declined
	  return HttpResponse('not Cool!')


