from django.http.response import HttpResponse
from django.shortcuts import render
from Trends.models import beeptimetrends , individualbeeptrends ,TrendsUpdateLastTime
from Trends import Constants
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models.query import QuerySet
import json
import Platform
from Platform import utils
from Trends.calc_trends import calc_trends
from Beep.models import Beep
from Platform.utils import MySerialiser
from django.db.models import Sum

# Create your views here.

# input:
# trend_type : 1 #Daily 2 #Weekly
# top_num : 20
def getTimeTrends(request):
    trend_type_req = request.GET[Constants.TrendServerConstants.TREND_TYPE]
    top_num = request.GET[Constants.TrendServerConstants.TOP_NUM]

    #check if we need to recalc trends
    thistypedata = TrendsUpdateLastTime.objects.get(trend_type = trend_type_req)
    lastupdatetime = thistypedata.last_update_time
    frequency_of_update = thistypedata.freq # in minutes
    if timezone.now() > lastupdatetime + timedelta(minutes=frequency_of_update):
        calc_trends(trend_type_req)

    this_trend_type_all_rows = beeptimetrends.objects.filter(trend_type = trend_type_req)
    totalbeeps = this_trend_type_all_rows.aggregate(Sum("beep_freq"))['beep_freq__sum']
    newbeeps = this_trend_type_all_rows.aggregate(Sum("is_new"))['is_new__sum']

    output = this_trend_type_all_rows.order_by('-beep_freq')[:top_num]
    beeplist =  list()
    for row in output:
        beepoutput = Beep.objects.get(beepid=row.beep_id)
        beepoutput.rebeeps = row.beep_freq
        beeplist.append(beepoutput)


    serializers = MySerialiser()
    jsondata = serializers.serialize(beeplist)
    jsondata = dict({"BeepList":jsondata,"new_num":newbeeps,"total_num":totalbeeps,"trend_type":trend_type_req})
    httpoutput = utils.successJson(jsondata)
    return HttpResponse(httpoutput,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

#periodically update trends
def updateTimeTrends(request):
    data = json.loads(request.read())
    trend_type = data[Constants.TrendServerConstants.TREND_TYPE]
    calc_trends(trend_type)
    return



