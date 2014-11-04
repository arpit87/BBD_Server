from django.http.response import HttpResponse
from Chat import Constants
import dict2xml
import logging
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json
import requests

logger = logging.getLogger(__name__)


# Create your views here.
@csrf_exempt
def createChatUser(request):
    print("creating chat user")
    data = json.loads(request.read())
    logger.debug(data)
    chatusername = data[Constants.ChatServerConstants.CHATUSERNAME]
    chatpassword = data[Constants.ChatServerConstants.CHATPASSWORD]
    url = 'http://127.0.0.1:9090/plugins/userService/users'

    data = {"username": chatusername,
            "password": chatpassword,
    }

    xmldata = dict2xml.dict2xml(data, wrap='user', indent="   ")
    req = requests.post(url, data=xmldata, headers={'Content-Type': 'application/xml',
                                                      'Authorization': Constants.OpenfireConstants.SECRETKEY})

    if req.status_code == 400:
        #put req
        req = requests.put(url+"/"+chatusername, data=xmldata, headers={'Content-Type': 'application/xml',
                                                      'Authorization': Constants.OpenfireConstants.SECRETKEY})

    return HttpResponse(req.status_code)




