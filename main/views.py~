from django.shortcuts import render
from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from ajax_select.fields import AutoCompleteField
#from main.forms import StreetsForm
from django.http import HttpResponseRedirect
from twilio.rest import TwilioRestClient
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import MyProfile
from django.contrib import messages
from django.utils.translation import ugettext as _

# Create your views here.
class SearchForm(forms.Form):

    q = AutoCompleteField(
            'street',
            required=True,
            help_text="Autocomplete will suggest clichs about cats, but you can enter anything you like.",
            label="Favorite Street",
            attrs={'size': 100}
            )

import pdb
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
    if request.POST and request.is_ajax():
	    mobile_number = request.POST.get('mobile_number', "").split()
	    mobile_number = '+374' + ''.join([mobile_number[0]]+mobile_number[1].split('-'))[1:]
	    if not mobile_number:
		return HttpResponse("No mobile number", content_type='text/plain', status=403)

	    pin = _get_pin()

	    # store the PIN in the cache for later verification.
	    #request.session['pin'] = pin # valid for 24 hrs

	    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	    message = client.messages.create(
		                body="%s" % pin,
		                to=mobile_number,
		                from_=settings.TWILIO_FROM_NUMBER,
		            )
	    return HttpResponse(json.dumps({'pin': pin}), content_type='application/json')

def set_user_balance(u, new_balance):
	b = MyProfile.objects.filter(user=u)[0]
	b.balance = new_balance
	b.save()
def get_user_balance(u):
	return MyProfile.objects.filter(user=u)[0].balance
def get_user_mobile(u):
	return MyProfile.objects.filter(user=u)[0].mobile_number

import stripe
import pdb
import json

def process_token(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY
	u = User.objects.filter(username=request.user)[0]
	# Get the credit card details submitted by the form
	#pdb.set_trace()	
	token = request.POST['token']
	amountAMD = request.POST['amountAMD']
	#pdb.set_trace()
	
	# Create the charge on Stripe's servers - this will charge the user's card
	try:
	  charge = stripe.Charge.create(
	      amount=amountAMD, # amount in cents, again
	      currency="amd",
	      card=token,
	      description="payinguser@example.com"
	  )
	  
	  balance = get_user_balance(u)
	  new_balance = balance + int(amountAMD) / 100
	  set_user_balance(u, new_balance)
	  return HttpResponse(json.dumps({'new_balance': str(new_balance)}), content_type = 'application/json')
	except stripe.CardError, e:
	  # The card has been declined
	  return HttpResponse('not Cool!')


from datetime import datetime
from happenings.models import (Cancellation, Event)
from django.template.defaultfilters import slugify
from django.views.decorators.csrf import csrf_exempt

def cancelEvent(request):
	SINGLE_FARE = 350.0
	if request.method == 'POST':
		e_id = request.POST['event_id']
		
		dt_tm = request.POST['date']
		butt_id = request.POST['butt_id']
		date = dt_tm.rsplit(',',1)[0] #splits into 2 parts and takes the first one
		#slugified = slugify(date)
		d = datetime.strptime(date, '%b. %d, %Y')
		ev = Event.objects.get(id=e_id)

		u = User.objects.filter(username=request.user)[0]
		balance = u.profile.balance
	  	#balance = get_user_balance(u)
	  	
	  	new_balance = balance + SINGLE_FARE * int(ev.passanger_number)
	  	#set_user_balance(u, new_balance)
	  	u.profile.balance = new_balance
        	u.profile.save()
		
		
		c = Cancellation(event=ev, reason='',date=d)
		c.save()
		return HttpResponse(json.dumps({'butt_id':butt_id, 'new_balance': new_balance}), content_type = 'application/json')

from main.forms import FeedbackForm
from main.models import Feedback
from happenings.models import Event
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from mezzanine.utils.models import get_user_model

User = get_user_model()

def save_feedback(request, event_id):
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        	#pdb.set_trace()
		event = Event.objects.get(id=event_id)
		fb = Feedback(event=event, user=request.user)
        	form = FeedbackForm(request.POST,instance=fb)
        # check whether it's valid:
        	if form.is_valid():
            	# process the data in form.cleaned_data as required
            		form.save()
            	# redirect to a new URL:
			messages.info(request, _("Your feedback is saved. Thank you!"))
            		return HttpResponseRedirect('/users/'+request.user.username)
		else:
			#rendered = render_to_string('includes/feedback.html', {'form': form, 'event_id': event_id})
			
			#return HttpResponse(json.dumps({'rendered':rendered}), content_type = 'application/json')
			lookup = {"username__iexact": request.user.username, "is_active": True}
			context = {"profile_user": get_object_or_404(User, **lookup)}
			messages.error(request, _("Your feedback has not been saved. Please fill in both fields."))
			return render(request,'accounts/account_profile.html', context)
    	# if a GET (or any other method) we'll create a blank form
    	else:
        	form = FeedbackForm()

	return render(request,'includes/feedback.html',{'form':form, 'event_id': event_id})

@csrf_exempt
def ppl_return(request):
	amount = username = error = ""
	if request.method == 'POST':
		amount, username = request.POST['custom'].split(',')
		#return HttpResponse('Your account has been recharged by '+request.POST['custom'].split(',')[0]+' AMD')
	else:
		error = "error"
		#return HttpResponse('request method is: '+request.method+'<br/> request is: ')
	return render(request,"paypal.html",{'amount': amount, 'username': username, 'error': error})

@csrf_exempt
def cancel(request):
	return render(request,"paypal_cancel.html")
	
from main.forms import ContactusForm

def contactus(request):
	if request.method == 'POST':
        	form = ContactusForm(request.POST)
        # check whether it's valid:
        	if form.is_valid():
            	# process the data in form.cleaned_data as required
            		form.save()
            	# redirect to a new URL:
			messages.info(request, _("We received your message, we will respond shortly. Thank you!"))
		else:
			messages.error(request, _("Your message has not been sent. Please fill in all the fields."))
    	# if a GET (or any other method) we'll create a blank form
    	else:
        	form = ContactusForm()

	return render(request,'index.html',{'form':form})
