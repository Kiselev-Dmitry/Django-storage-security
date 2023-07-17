from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.visit_time_check import get_duration
from datacenter.visit_time_check import format_duration


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        passcard = visit.passcard
        who_entered = passcard.owner_name
        entered_at = localtime(visit.entered_at)
        seconds = get_duration(visit)
        duration = format_duration(seconds)
        visit_info = {
            'who_entered': who_entered,
            'entered_at': entered_at,
            'duration': duration,
        }
        non_closed_visits.append(visit_info)
    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
