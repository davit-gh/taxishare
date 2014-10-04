from ajax_select import make_ajax_field
from ajax_select import make_ajax_form
from main.models import SourceDest
from main.models import Streets
from django.forms import ModelForm
from ajax_select.fields import AutoCompleteField
from ajax_select.fields import AutoCompleteWidget
from django import forms
from functools import partial
DateInput = partial(forms.DateInput, )

# Form Fields
from django.forms.util import from_current_timezone
from django.forms.util import to_current_timezone
from django.utils import timezone

class TzAwareTimeField(forms.fields.TimeField):
    def prepare_value(self, value):
        if isinstance(value, datetime.datetime):
            value = to_current_timezone(value).time()
        return super(TzAwareTimeField, self).prepare_value(value)

    def clean(self, value):
        value =  super(TzAwareTimeField, self).to_python(value)
        dt = to_current_timezone(timezone.now())
        return dt.replace(
            hour=value.hour, minute=value.minute,
            second=value.second, microsecond=value.microsecond)


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
