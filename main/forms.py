from ajax_select import make_ajax_field
from ajax_select import make_ajax_form
from main.models import SourceDest
from main.models import Streets
from django.forms import ModelForm
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
	source 	    = AutoCompleteField('street', required=True, help_text=None)
	destination = AutoCompleteField('street', required=True, help_text=None)
	repeat 	    = forms.ChoiceField(widget=forms.Select(attrs={'id': "id_repeat", 'class': 'repeatClass', 'onchange':'getRepeat(this);'}), choices=REPEAT_CHOICES, initial='NEVER')
	class Meta:
 		model = Event
		fields = ['source','destination','start_date','repeat','end_repeat']
		widgets = {
            		'start_date': DateTimeWidget(attrs={'id':"id_source"}, options={'startDate':'+1d'}, bootstrap_version=3),
	    		'end_repeat': DateWidget(attrs={'id':"id_end_repeat"}, options={'startDate':'+2d'}, bootstrap_version=3)
        	}
	def clean_source(self):
		source = self.cleaned_data['source']
		obj = Streets.objects.filter(name_hy=source)[0]
		return obj

	def clean_destination(self):
		dest = self.cleaned_data['destination']
		obj = Streets.objects.filter(name_hy=dest)[0]
		return obj

class StreetsForm(ModelForm):
    #form = make_ajax_form(SourceDest, {'streets': 'street'})
    book_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}, format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    timestamp = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'timepicker'}, format='%H:%M'))
    source 	= AutoCompleteField('street', required=True, help_text=None)
    destination = AutoCompleteField('street', required=True, help_text=None)
    class Meta:
        model = SourceDest
	fields = ['source','destination','book_date', 'timestamp']
	
	
    #haylabel  = make_ajax_field(SourceDest, 'name_hy', 'haystreet', help_text='Need help?')
    def clean_source(self):
	source = self.cleaned_data['source']
	obj = Streets.objects.filter(name_hy=source)[0]
	return obj

    def clean_destination(self):
	dest = self.cleaned_data['destination']
	obj = Streets.objects.filter(name_hy=dest)[0]
	return obj
