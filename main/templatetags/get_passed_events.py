from __future__ import unicode_literals

import heapq

from django.template import Library
from django.utils import timezone

from happenings.utils.upcoming import UpcomingEvents
from happenings.models import Event
from happenings.utils.common import now

register = Library()

@register.inclusion_tag('happenings/partials/passed_events.html')
def passed_events(request, now=timezone.localtime(timezone.now()), days_ago=90, num=5):
    start = now - timezone.timedelta(days=days_ago)
    
    all_passed = (UpcomingEvents(x, now, days_ago, num).get_passed_events()
                    for x in Event.objects.passed(now).filter(created_by=request.user))
    #pdb.set_trace()
    passed = heapq.nsmallest(
        num,
        (item for sublist in all_passed for item in sublist),
        key=lambda x: x[0]
    )
    return {'passed_events': passed}
