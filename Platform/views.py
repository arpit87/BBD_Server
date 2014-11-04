from Platform.models import APPDATA
import Beep.Constants
import Platform.Constants
import json
from django.http import HttpResponse
from django.template import Context, loader


def authenticateURL(request):
    if Platform.Constants.ISTESTMODE==True:
        return True

    data = json.loads(request.read())
    if request.method == 'POST':
        appuuid_req = data[Beep.Constants.BeepServerConstants.APPUUID]
        bbdid_req = data[Beep.Constants.BeepServerConstants.BBD_ID]
        appdetails = APPDATA.objects.get(bbdid = bbdid_req)
        if appdetails.appuuid == appuuid_req:
            return True


    if request.method == 'GET':
        appuuid_req = data[Beep.Constants.BeepServerConstants.APPUUID]
        bbdid_req = data[Beep.Constants.BeepServerConstants.BBD_ID]
        appdetals = APPDATA.objects.get(bbdid = bbdid_req)
        if appdetals.appuuid == appuuid_req:
            return True

    return False

def index(request):
    template = loader.get_template('Platform/index.html')
    c = Context({})
    return HttpResponse(template.render(c))	
