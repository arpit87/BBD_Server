# Create your tests here.
#teST MODELS
from django.test import TestCase
from django.utils import timezone
from Beep.models import Beep,SentBeep
from Beep import Constants
import Platform.Constants
import json
from django.core.serializers import serialize,deserialize

class BeepTestCase(TestCase):
    def test_createBeep(self):
        input = json.dumps({Constants.BeepServerConstants.BBD_ID:1000,
                      Constants.BeepServerConstants.BEEP_STR:"bhak bhosdi",
                      Constants.BeepServerConstants.BEEPLEVEL:3})
        response = self.client.post('/Beep/createBeep/',input, 'application/json')
        beep = Beep.objects.get(pk=1)
        self.assertEqual(beep.beep_str,"Bhak Bhosadi")
        self.assertEqual(beep.created_by,1001)


class GetBeepListTestCase(TestCase):
    def test_getBeepList(self):
        input = dict({Constants.BeepServerConstants.NUMBEEPS:4,Constants.BeepServerConstants.BEEPLEVEL:3})
        response = self.client.get('/Beep/getBeepList/',input)
        self.assertEqual(response.status_code,200)
        print(response.content)


    def test_getMyBeepList(self):
        input = dict({Constants.BeepServerConstants.NUMBEEPS:4,Constants.BeepServerConstants.BBD_ID:1001})
        response = self.client.get('/Beep/getMyBeepList/',input)
        self.assertEqual(response.status_code,200)
        print(response.content)


class SendBeepTestCase(TestCase):
    def test_sendbeep(self):
        input = json.dumps({Constants.BeepServerConstants.BEEP_ID:1,
                        Constants.BeepServerConstants.BBD_ID:1,
                      Constants.BeepServerConstants.FRIEND_BBD_ID:2})
        response = self.client.post('/Beep/sendBeep/',input, 'application/json')
        self.assertEqual(response.status_code,200)

