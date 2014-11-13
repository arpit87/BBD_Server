__author__ = 'ubuntu'
from Beep.models import SentBeep , Beep
from datetime import datetime , timedelta
from django.utils import timezone
from django.db.models import Count ,ObjectDoesNotExist
from Trends.Constants import TimeConstants
from Trends.models import beeptimetrends ,individualbeeptrends , TrendsUpdateLastTime


def calc_trends(type_input):
    type = int(type_input) #this comes in as unicode
    if type == TimeConstants.DAILY:
        eligiblebeeps = SentBeep.objects.filter(date_time__gt=datetime.now()-timedelta(days=1))

    if type == TimeConstants.WEEKLY:
        eligiblebeeps = SentBeep.objects.filter(date_time__gt=datetime.now()-timedelta(days=7))

    if type == TimeConstants.MONTHLY:
        eligiblebeeps = SentBeep.objects.filter(date_time__gt=datetime.now()-timedelta(days=30))

    eligiblebeeps_freq = eligiblebeeps.values("beep").annotate(beep_freq=Count('beep')).order_by()


    for item in eligiblebeeps_freq:
        try:
            this_trend = beeptimetrends.objects.get(beep=item['beep'],trend_type=type)
            this_trend.beep_freq = item['beep_freq']
        except ObjectDoesNotExist:
            this_trend = beeptimetrends(beep = Beep.objects.get(beepid=item['beep']),trend_type = type,beep_freq=item['beep_freq'])
        this_trend.save()

    #update updatetime keeper table
    thisTrendRow = TrendsUpdateLastTime.objects.get(trend_type=type)
    thisTrendRow.last_update_time = timezone.now()
    thisTrendRow.save()
    return

