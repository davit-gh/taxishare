from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
#from main.models import SourceDest
from main.models import *
from happenings.models import Event
from happenings.models import Cancellation
from mezzanine.core.admin import TabularDynamicInlineAdmin


class OrderAdmin(admin.ModelAdmin):
	list_display=('source','destination','book_date','timestamp')

class CancellationAdmin(TabularDynamicInlineAdmin):
	model=Cancellation

class EventAdmin(admin.ModelAdmin):
	inlines = [CancellationAdmin,]
	list_display=('source','destination','start_date','created_by', 'repeat', 'end_repeat', 'title', 'passanger_number')

admin.site.register(Event, EventAdmin)
#admin.site.register(SourceDest, OrderAdmin)

from main.models import Feedback
class FeedbackAdmin(admin.ModelAdmin):
	list_display=('title','feedback_desc','feedback_date','user', 'event')

admin.site.register(Feedback,FeedbackAdmin)

from main.models import Contactus
class ContactusAdmin(admin.ModelAdmin):
	list_display=('name','email','title','description', 'message_date')

admin.site.register(Contactus,ContactusAdmin)

from main.models import Inboundmail
class InboundmailAdmin(admin.ModelAdmin):
        list_display=('send_date', 'subject', 'html_body', 'reply_to', 'sender')

admin.site.register(Inboundmail, InboundmailAdmin)
