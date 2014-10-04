from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from main.models import SourceDest
from main.models import *


class StreetAdmin(AjaxSelectAdmin):
    # create an ajax form class using the factory function
    #                     model,fieldlist,   [form superclass]
    form = make_ajax_form(Streets,{'name_en':'street'})
admin.site.register(Streets,StreetAdmin)

class OrderAdmin(admin.ModelAdmin):
	list_display=('source','destination','book_date','timestamp')

admin.site.register(SourceDest, OrderAdmin)

