from ajax_select import make_ajax_field
from ajax_select import make_ajax_form
#from main.models import SourceDest
from happenings.models import Streets
from django.forms import ModelForm, Textarea
from ajax_select.fields import AutoCompleteField
from ajax_select.fields import AutoCompleteWidget
from django import forms
from functools import partial
from django.utils.translation import ugettext as _

DateInput = partial(forms.DateInput, )

# Form Fields
from django.forms.util import from_current_timezone
from django.forms.util import to_current_timezone
from django.utils import timezone
from happenings.models import Event
from datetimewidget.widgets import DateTimeWidget
from datetimewidget.widgets import DateWidget
from main.models import Feedback
from main.models import MyProfile
from main.models import Contactus
import datetime
import pdb

class EventForm(ModelForm):

	REPEAT_CHOICES = (
            ('NEVER', _('Never')),
            ('DAILY', _('Every Day')),
            ('WEEKDAY', _('Every Weekday')),
            ('WEEKLY', _('Every Week')),
            ('BIWEEKLY', _('Every 2 Weeks')),
            ('MONTHLY', _('Every Month')),
            ('YEARLY', _('Every Year')),
        )

	PASSANGER_NUMBER_CHOICES = (
            ('1', 1),
            ('2', 2),
            ('3', 3),
        )
    
 	PAYMENT_CHOICES = (
	    ('1', _("With cash")),
        ('2', _("Use My Balance")),
	)
	source 	    = AutoCompleteField('street', label=_('Source'), required=True, help_text=None)
	destination = AutoCompleteField('street', label=_('Destination'), required=True, help_text=None)
	repeat 	    = forms.ChoiceField(label=_("Repeat"), widget=forms.Select(attrs={'id': "id_repeat", 'class': 'repeatClass', 'onchange':'getRepeat(this);'}), choices=REPEAT_CHOICES, initial='NEVER')
	passanger_number = forms.ChoiceField(label=_("How many?"), widget=forms.Select(attrs={'id': "id_passanger_number", 'class': 'passnumClass'}), choices=PASSANGER_NUMBER_CHOICES, initial='ONE')
	payment_method = forms.ChoiceField(label=_("Payment Method"), choices=PAYMENT_CHOICES, widget=forms.RadioSelect(), initial='1')
	class Meta:
 		model = Event
		fields = ['source', 'destination', 'source_detail', 'destination_detail', 'start_date','repeat','passanger_number', 'payment_method', 'end_repeat']

		widgets = {
            		'start_date': DateTimeWidget(attrs={'id':"id_source"}, options={'startDate':'+1d'}, bootstrap_version=3),
	    		'end_repeat': DateWidget(attrs={'id':"id_end_repeat"}, options={'startDate':'+2d'}, bootstrap_version=3),
	    		'source_detail':forms.Textarea(attrs={'rows': 10, 'style': 'height: 5em; resize: none;', 'placeholder':_("around market")}),
	    		'destination_detail':forms.Textarea(attrs={'rows': 10, 'style': 'height: 5em; resize: none;', 'placeholder':_('around university')})
        	}
	def clean_source(self):
		source = self.cleaned_data['source']
		obj, created = Streets.objects.get_or_create(name_en=source, defaults={'name_hy': 'not set'})
		return obj

	def clean_destination(self):
		dest = self.cleaned_data['destination']
		obj, created = Streets.objects.get_or_create(name_en=dest, defaults={'name_hy': 'not set'})
		return obj

	def clean_start_date(self):
		start_datetime = self.cleaned_data["start_date"]
		start_date = start_datetime.date()
		curr_date = datetime.datetime.now().date()
		if start_date < curr_date + datetime.timedelta(days=1):
		    raise forms.ValidationError(_("Please enter future date."), code='invalid')
		return start_datetime

#class StreetsForm(ModelForm):
#    #form = make_ajax_form(SourceDest, {'streets': 'street'})
#    book_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}, format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
#    timestamp = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'timepicker'}, format='%H:%M'))
#    source 	= AutoCompleteField('street', required=True, help_text=None)
#    destination = AutoCompleteField('street', required=True, help_text=None)
#    class Meta:
#        model = SourceDest
#	fields = ['source','destination','book_date', 'timestamp']
	
	
    #haylabel  = make_ajax_field(SourceDest, 'name_hy', 'haystreet', help_text='Need help?')
#    def clean_source(self):
#	source = self.cleaned_data['source']
#	obj = Streets.objects.filter(name_hy=source)[0]
#	return obj
#
#    def clean_destination(self):
#	dest = self.cleaned_data['destination']
#	obj = Streets.objects.filter(name_hy=dest)[0]
#	return obj

from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.widgets import ValueHiddenInput, ReservedValueHiddenInput
 
class PayPalPaymentsFormCustom(PayPalPaymentsForm):
	image_url = forms.CharField(widget=ValueHiddenInput)
	custom = forms.CharField(widget=ValueHiddenInput)
	hosted_button_id = forms.CharField(widget=ValueHiddenInput)


class FeedbackForm(ModelForm):
	class Meta:
		model = Feedback
		fields = ['title', 'feedback_desc']
		widgets = {
			'feedback_text': Textarea(attrs={
				'placeholder':_('Thank you for your comment!')
			}),
		}

class ContactusForm(ModelForm):
	class Meta:
		model = Contactus
		fields = ['name', 'email', 'title', 'description']
		
