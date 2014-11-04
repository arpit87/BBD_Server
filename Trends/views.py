from django.http.response import HttpResponse
from django.shortcuts import render
from Trends.models import beeptimetrends , individualbeeptrends
from Trends import Constants
from datetime import datetime , timedelta
from django.db.models.query import QuerySet
import json
# Create your views here.

# input:
# trend_type : 1 #Daily 2 #Weekly
# top_num : 20
def getTimeTrends(request):
    data = json.loads(request.read())
    trend_type_req = data[Constants.TrendServerConstants.TREND_TYPE]
    top_num = data[Constants.TrendServerConstants.TOP_NUM]
    this_trend_type_all_rows = beeptimetrends.objects.filter(trend_type = trend_type_req)
    top_rows = this_trend_type_all_rows.order_by('beep_freq')[:20]
    return HttpResponse("Success")

#periodically update trends
def setTimeTrends(trend_algo, data):
    """

    :type data: QuerySet
    """
    time_label = trend_algo.getTimeLabel()
    freq_label = trend_algo.getFreqLabel()
    trend_type = trend_algo.getTrendType()
    if trend_type == Constants.TimeConstants.DAILY:
        cutofftime = datetime.now() - timedelta(days=1)
    elif trend_type == Constants.TimeConstants.WEEKLY:
        cutofftime  = datetime.now() - timedelta(days=7)
    elif trend_type == Constants.TimeConstants.MONTHLY:
        cutofftime = datetime.now() - timedelta(days=30)

    elegible_data = data.filter(time_label > cutofftime)
    ordered_data = elegible_data.order_by(freq_label)
    return ordered_data


