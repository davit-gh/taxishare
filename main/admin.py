from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from main.models import SourceDest
from main.models import *
from happenings.models import Event

class StreetAdmin(AjaxSelectAdmin):
    # create an ajax form class using the factory function
    #                     model,fieldlist,   [form superclass]
    form = make_ajax_form(Streets,{'name_en':'street'})
admin.site.register(Streets,StreetAdmin)

class OrderAdmin(admin.ModelAdmin):
	list_display=('source','destination','book_date','timestamp')

class EventAdmin(admin.ModelAdmin):
	list_display=('source','destination','start_date','end_date', 'repeat', 'end_repeat', 'title', 'description')

admin.site.register(Event, EventAdmin)
admin.site.register(SourceDest, OrderAdmin)

from main.models import Feedback
class FeedbackAdmin(admin.ModelAdmin):
	list_display=('title','feedback_desc','feedback_date','user', 'event')

admin.site.register(Feedback,FeedbackAdmin)

from main.models import Contactus
class ContactusAdmin(admin.ModelAdmin):
	list_display=('name','email','title','description', 'message_date')

admin.site.register(Contactus,ContactusAdmin)
