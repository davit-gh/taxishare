from main.models import MyProfile
from django.contrib.auth.models import User
from mezzanine import template
register = template.Library()

@register.as_tag
def get_user_balance(request):
    u=User.objects.get(username=request.user.username)
    balance=MyProfile.objects.filter(user=u)[0].balance
    return balance



