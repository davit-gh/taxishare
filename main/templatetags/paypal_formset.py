from main.forms import ContactusForm
from mezzanine import template
register = template.Library()

from main.forms import PayPalPaymentsFormCustom
from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
import pdb
@register.as_tag
def get_ppl_formset(request):

    # What you want the button to do.
    paypal_dict1 = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "0.72",
        "item_name": "300 dram",
	"custom": "300,"+request.user.username,
	"hosted_button_id": "JL7L94278G4C8",
        "notify_url": "http://armeninio.pythonanywhere.com" + reverse('paypal-ipn'),
        "return_url": "http://armeninio.pythonanywhere.com/ppl_return/",
        "cancel_return": "http://armeninio.pythonanywhere.com/your-cancel-location/",
    }
    paypal_dict2 = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "1.44",
        "item_name": "600 dram",
	"custom": "600,"+request.user.username,
        "notify_url": "http://armeninio.pythonanywhere.com" + reverse('paypal-ipn'),
        "return_url": "http://armeninio.pythonanywhere.com/ppl_return/",
        "cancel_return": "http://armeninio.pythonanywhere.com/your-cancel-location/",
    }
    paypal_dict3 = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "2.88",
        "item_name": "1200 dram",
	"custom": "1200,"+request.user.username,
        "notify_url": "http://armeninio.pythonanywhere.com" + reverse('paypal-ipn'),
        "return_url": "http://armeninio.pythonanywhere.com/ppl_return/",
        "cancel_return": "http://armeninio.pythonanywhere.com/your-cancel-location/",
    }
    paypal_dict4 = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "5.76",
        "item_name": "2400 dram",
	"custom": "2400,"+request.user.username,
        "notify_url": "http://armeninio.pythonanywhere.com" + reverse('paypal-ipn'),
        "return_url": "http://armeninio.pythonanywhere.com/ppl_return/",
        "cancel_return": "http://armeninio.pythonanywhere.com/your-cancel-location/",
    }
    paypal_dict5 = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "11.52",
        "item_name": "4800 dram",
	"custom": "4800,"+request.user.username,
        "notify_url": "http://armeninio.pythonanywhere.com" + reverse('paypal-ipn'),
        "return_url": "http://armeninio.pythonanywhere.com/ppl_return/",
        "cancel_return": "http://armeninio.pythonanywhere.com/your-cancel-location/",
    }
    paypal_dict6 = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "14.6",
        "item_name": "6000 dram",
        "invoice": "unique-invoice-id",
	"custom": "6000,"+request.user.username,
        "notify_url": "http://armeninio.pythonanywhere.com" + reverse('paypal-ipn'),
        "return_url": "http://armeninio.pythonanywhere.com/ppl_return/",
        "cancel_return": "http://armeninio.pythonanywhere.com/your-cancel-location/",
    }

#    PaypalFormSet = formset_factory(PayPalPaymentsFormCustom, max_num=6)
#    formset = PaypalFormSet(initial=[paypal_dict1, paypal_dict2, paypal_dict3, paypal_dict4, paypal_dict5, paypal_dict6])
    # Create the instance.
    form1 = PayPalPaymentsFormCustom(initial=paypal_dict1)
    form2 = PayPalPaymentsFormCustom(initial=paypal_dict2)
    form3 = PayPalPaymentsFormCustom(initial=paypal_dict3)    
    form4 = PayPalPaymentsFormCustom(initial=paypal_dict4)
    form5 = PayPalPaymentsFormCustom(initial=paypal_dict5)
    form6 = PayPalPaymentsFormCustom(initial=paypal_dict6)
    context = [(form1,'img/ppl/300.JPG'), (form2, 'img/ppl/600.JPG'), (form3, 'img/ppl/1200_1.JPG'), (form4, 'img/ppl/2400.JPG'), (form5, 'img/ppl/4800.JPG'), (form6, 'img/ppl/6000.JPG')]
    return context

