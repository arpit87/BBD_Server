# Create your views here.
from django.http import HttpResponse

from Beep import Constants
from Beep.models import Beep,SentBeep
from Platform import utils
from Platform.views import authenticateURL
import Platform.Constants
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

#getbeep api
@csrf_exempt
def getBeep(request):
    logger.debug('get beep')
    if authenticateURL(request)==False:
        httpresonse = utils.errorJson("Error authenticating user")
        return HttpResponse(httpresonse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

    data = json.loads(request.read())
    beepidrequested = data[Constants.BeepServerConstants.BEEP_ID]
    output = Beep.objects.get(beepid=beepidrequested)
    httpresonse = utils.successJson(output)
    return HttpResponse(httpresonse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)



#create beep returns beep_id
@csrf_exempt
def createBeep(request):
    logger.debug('create beep')
    if authenticateURL(request)==False:
        httpresponse = utils.errorJson("Error authenticating user")
        return HttpResponse(httpresponse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

    data = json.loads(request.read())
    beepstr_req = data[Constants.BeepServerConstants.BEEP_STR]
    bbdid_req = data[Constants.BeepServerConstants.BBD_ID]
    beeplevel_req = data[Constants.BeepServerConstants.BEEPLEVEL]
    beep = Beep(created_by = bbdid_req,beep_str=beepstr_req,beeplevel=beeplevel_req)
    beep.save()

    returndata = dict({Constants.BeepServerConstants.BEEP_ID:beep.pk})
    httpresponse = utils.successJson(returndata)
    return HttpResponse(httpresponse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)


@csrf_exempt
def getBeepList(request):
    logger.debug('get beep list')
    if authenticateURL(request)==False:
        httpresonse = utils.errorJson("Error authenticating user")
        return HttpResponse(httpresonse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

    userlevel=request.GET[Constants.BeepServerConstants.BEEPLEVEL]
    numbeeps=request.GET[Constants.BeepServerConstants.NUMBEEPS]
    output = Beep.objects.all().filter(beeplevel__lt = userlevel).order_by('?')[:numbeeps]
    #jsondata = serializers.serialize('json',output)
    jsondata = list(output.values())
    jsondata = dict({"BeepList":jsondata})
    httpoutput = utils.successJson(jsondata)
    return HttpResponse(httpoutput,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

@csrf_exempt
def sendBeep(request):
    if authenticateURL(request)==False:
        httpresonse = utils.errorJson("Error authenticating user")
        return HttpResponse(httpresonse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

    data = json.loads(request.read())
    beep_id = data[Constants.BeepServerConstants.BEEP_ID]
    from_bbdid = data[Constants.BeepServerConstants.BBD_ID]
    to_bbdid = data[Constants.BeepServerConstants.FRIEND_BBD_ID]
    datentime =datetime.now()

    sentbeep = SentBeep(from_id=from_bbdid, to_id=to_bbdid, beepid=beep_id, date_time=datentime)
    sentbeep.save()

    returndata = dict()
    httpresponse = utils.successJson(returndata)
    return HttpResponse(httpresponse,content_type=Platform.Constants.RESPONSE_JSON_TYPE)
