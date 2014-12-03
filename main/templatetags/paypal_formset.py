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
        "amount": "0.792",
        "item_name": "350 dram",
	"custom": "350,"+request.user.username,
	"hosted_button_id": "JL7L94278G4C8",
        "notify_url": "http://www.taxinmiasin.com" + reverse('paypal-ipn'),
        "return_url": "http://www.taxinmiasin.com/ppl_return/",
        "cancel_return": "http://www.taxinmiasin.com/your-cancel-location/",
    }
    paypal_dict2 = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "1.58",
        "item_name": "700 dram",
	"custom": "700,"+request.user.username,
        "notify_url": "http://www.taxinmiasin.com" + reverse('paypal-ipn'),
        "return_url": "http://www.taxinmiasin.com/ppl_return/",
        "cancel_return": "http://www.taxinmiasin.com/your-cancel-location/",
    }
    paypal_dict3 = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "3.17",
        "item_name": "1400 dram",
	"custom": "1400,"+request.user.username,
        "notify_url": "http://www.taxinmiasin.com" + reverse('paypal-ipn'),
        "return_url": "http://www.taxinmiasin.com/ppl_return/",
        "cancel_return": "http://www.taxinmiasin.com/your-cancel-location/",
    }
    paypal_dict4 = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "6.34",
        "item_name": "2800 dram",
	"custom": "2800,"+request.user.username,
        "notify_url": "http://www.taxinmiasin.com" + reverse('paypal-ipn'),
        "return_url": "http://www.taxinmiasin.com/ppl_return/",
        "cancel_return": "http://www.taxinmiasin.com/your-cancel-location/",
    }
    paypal_dict5 = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "12.67",
        "item_name": "5600 dram",
	"custom": "5600,"+request.user.username,
        "notify_url": "http://www.taxinmiasin.com" + reverse('paypal-ipn'),
        "return_url": "http://www.taxinmiasin.com/ppl_return/",
        "cancel_return": "http://www.taxinmiasin.com/your-cancel-location/",
    }
    paypal_dict6 = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "15.84",
        "item_name": "7000 dram",
        "invoice": "7000",
	"custom": "7000,"+request.user.username,
        "notify_url": "http://www.taxinmiasin.com" + reverse('paypal-ipn'),
        "return_url": "http://www.taxinmiasin.com/ppl_return/",
        "cancel_return": "http://www.taxinmiasin.com/your-cancel-location/",
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
    context = [(form1,'img/ppl/ppl/350.jpg'), (form2, 'img/ppl/ppl/700.jpg'), (form3, 'img/ppl/ppl/1400.jpg'), (form4, 'img/ppl/ppl/2800_1.jpg'), (form5, 'img/ppl/ppl/5600_1.jpg'), (form6, 'img/ppl/ppl/7000.jpg')]
    return context

