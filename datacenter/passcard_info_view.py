from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime
from datacenter.visit_time_check import get_duration
from datacenter.visit_time_check import format_duration
from datacenter.visit_time_check import is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        entered_at = localtime(visit.entered_at)
        duration = format_duration(get_duration(visit))
        is_strange = is_visit_long(visit)
        this_passcard_visits.append({
            'entered_at': entered_at,
            'duration': duration,
            'is_strange': is_strange
        })
    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
