from main.models import MyProfile
from django.contrib.auth.models import User
from mezzanine import template
register = template.Library()

@register.as_tag
def get_user_balance(request):
    u=User.objects.filter(username=request.user)[0]
    balance=MyProfile.objects.filter(user=u)[0].balance
    return balance



