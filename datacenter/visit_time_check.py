from django.utils.timezone import localtime


def get_duration(visit):
    time_in = localtime(visit.entered_at)
    time_out = visit.leaved_at
    if time_out is None: time_out = localtime()
    delta = time_out - time_in
    return delta.total_seconds()


def format_duration(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return "{hrs}:{min}".format(hrs=hours, min=minutes)


def is_visit_long(visit, minutes=60):
    minutes_inside = get_duration(visit)/60
    return minutes_inside>minutes

