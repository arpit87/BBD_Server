__author__ = 'ubuntu'
from Beep.models import SentBeep , Beep
from datetime import  timedelta
from django.utils import timezone
from django.utils import timezone
from django.db.models import Count ,ObjectDoesNotExist
from Trends.Constants import TimeConstants
from Trends.models import beeptimetrends ,individualbeeptrends , TrendsUpdateLastTime


def calc_trends(type_input):
    type = int(type_input) #this comes in as unicode
    typetimedelta = 0
    if type == TimeConstants.DAILY:
        typetimedelta = timezone.now()-timedelta(days=1)
        eligiblebeeps = SentBeep.objects.filter(date_time__gt=typetimedelta)

    if type == TimeConstants.WEEKLY:
        typetimedelta = timezone.now()-timedelta(days=7)
        eligiblebeeps = SentBeep.objects.filter(date_time__gt=typetimedelta)

    if type == TimeConstants.MONTHLY:
        typetimedelta = timezone.now()-timedelta(days=30)
        eligiblebeeps = SentBeep.objects.filter(date_time__gt=typetimedelta)

    eligiblebeeps_freq = eligiblebeeps.values("beep").annotate(beep_freq=Count('beep')).order_by()


    for item in eligiblebeeps_freq:
        try:
            this_trend = beeptimetrends.objects.get(beep=item['beep'],trend_type=type)
            beep = Beep.objects.get(beepid=item['beep'])
            if beep.date_created > typetimedelta:
                this_trend.is_new = 1
            else:
                this_trend.is_new = 0
            this_trend.beep_freq = item['beep_freq']
        except ObjectDoesNotExist:
            this_trend = beeptimetrends(beep = Beep.objects.get(beepid=item['beep']),trend_type = type,beep_freq=item['beep_freq'])
            this_trend.is_new = 1
        this_trend.save()

    #update updatetime keeper table
    thisTrendRow = TrendsUpdateLastTime.objects.get(trend_type=type)
    thisTrendRow.last_update_time = timezone.now()
    thisTrendRow.save()
    return

