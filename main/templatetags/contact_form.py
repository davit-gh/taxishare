from main.forms import ContactusForm
from mezzanine import template
register = template.Library()

@register.as_tag
def get_contact_form(*args):
	return ContactusForm()
