# Create your views here.
import string
import random
from django.core.exceptions import ObjectDoesNotExist

from django.http.response import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

import Beep.Constants
from Platform import utils
from Platform.models import APPDATA

from User.models import UserDetails, Friend
from Platform.views import authenticateURL
import Chat.views
import Chat.Constants
import Platform.Constants
import User.Constants
import json
import requests
import logging
#import pdb; pdb.set_trace()

logger = logging.getLogger(__name__)
#request_logger = logging.getLogger('bbd.request')
@csrf_exempt
def createUser(request):
    logger.debug("creating usr")
    if authenticateURL(request) == False:
        httpresonse = utils.errorJson("Error authenticating user")
        return HttpResponse(httpresonse, content_type=Platform.Constants.RESPONSE_JSON_TYPE)

    data = json.loads(request.read())
    logger.debug("createUser:input:"+str(data))
    name_req = data[Beep.Constants.BeepServerConstants.USERNAME]
    uuid_req = data[Beep.Constants.BeepServerConstants.APPUUID]

    if name_req != "dev2118":
        logger.debug("Creting user:")
        datejoined_req = timezone.now().date()
        newuser = UserDetails(name=name_req, date_joined=datejoined_req)
        newuser.save()

        #enter authentication data
        authdata = APPDATA(appuuid=uuid_req, bbdid=newuser.bbdid)
        authdata.save()
    else:
        logger.debug("Returning dev profile")
        newuser = UserDetails.objects.get(bbdid=1001)
        authdata = APPDATA.objects.get(bbdid=1001)


    # create char user now
    chars = string.ascii_uppercase + string.digits
    chatuser =  str(newuser.bbdid)
    chatpass = ''.join(random.choice(chars) for _ in range(6))
    url = 'http://127.0.0.1:80/Chat/createChatUser/'
    jsondata = json.dumps({Chat.Constants.ChatServerConstants.CHATUSERNAME: chatuser,
              Chat.Constants.ChatServerConstants.CHATPASSWORD: chatpass})

    req = requests.post(url, data=jsondata,headers={'Content-Type':'application/json'})

    if req.status_code != 201 and req.status_code != 200:
        jsonResponse = utils.errorJson("Error creating User")
        return HttpResponse(jsonResponse,Platform.Constants.RESPONSE_JSON_TYPE,status=500)

    jsondata = dict({Beep.Constants.BeepServerConstants.BBD_ID:newuser.bbdid,
                     Chat.Constants.ChatServerConstants.CHATUSERNAME:chatuser,
                     Chat.Constants.ChatServerConstants.CHATPASSWORD:chatpass})
    if name_req == "dev2118":
        jsondata.update({"uuid":authdata.appuuid})

    httpoutput = utils.successJson(jsondata)
    logger.debug("createUser:output:"+str(httpoutput))
    return HttpResponse(httpoutput,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

@csrf_exempt
def addFriend(request):
    if authenticateURL(request) == False:
        return HttpResponse("Error authenticating user")

    data = json.loads(request.read())
    your_bbdid = data[Beep.Constants.BeepServerConstants.BBD_ID]
    friend_bbdid = data[Beep.Constants.BeepServerConstants.FRIEND_BBD_ID]
    try:
        friendObj = UserDetails.objects.get(bbdid=friend_bbdid)
    except ObjectDoesNotExist:
        httpoutput = utils.errorJson(dict())
        return HttpResponse(httpoutput,content_type=Platform.Constants.RESPONSE_JSON_TYPE)

    addfriend = Friend(bbdid=your_bbdid, friend_bbd_id=friend_bbdid)
    addfriend.save()
    friendnick = friendObj.name;
    jsondata = dict({User.Constants.UserServerConstants.FRIEND_NICK:friendnick,
                     User.Constants.UserServerConstants.FRIEND_BBD_ID:friend_bbdid})
    httpoutput = utils.successJson(jsondata)
    return HttpResponse(httpoutput,content_type=Platform.Constants.RESPONSE_JSON_TYPE)



