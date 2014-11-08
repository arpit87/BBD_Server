from django.test import TestCase



#Test models
from django.utils import timezone
from Beep import Constants
from User.models import UserDetails,Friend

class UserDetailsTestCase(TestCase):
    def setUp(self):
        UserDetails.objects.create(bbdid= 1,name="Arpit" ,date_joined=timezone.now().date())
        UserDetails.objects.create(bbdid= 2,name="Anshul" ,date_joined=timezone.now().date())
        UserDetails.objects.create(bbdid= 3,name="Varun" ,date_joined=timezone.now().date())

    def test_userdetails(self):
        arpitdetails = UserDetails.objects.get(bbdid = 1)
        self.assertEqual(arpitdetails.name , "Arpit")



class FriendTestCase(TestCase):
    def setUp(self):
        Friend.objects.create(bbdid = 1,friend_bbd_id=2)
        Friend.objects.create(bbdid = 1,friend_bbd_id=3)

    def test_friend(self):
        arpitfriends = Friend.objects.filter(bbdid = 1)
        friend_list_bbdid = [2,3]
        for friend in arpitfriends:
            self.assertTrue(friend.friend_bbd_id in friend_list_bbdid)


#Test URLS
from Platform.models import APPDATA
from User.models import Friend
import json
import Platform.Constants

class UserAPITestCase(TestCase):

    def test_createUser(self):
        inputval = json.dumps({Constants.BeepServerConstants.USERNAME:'Arpit', Constants.BeepServerConstants.APPUUID:'123'})
	print(inputval)
        response = self.client.post('/User/createUser/',inputval,'application/json')
        self.assertEqual(response.status_code,200)
        print(response.content)

    def test_addFriend(self):
        response = self.client.post('/User/addFriend/',json.dumps({Constants.BeepServerConstants.APPUUID:'123', Constants.BeepServerConstants.BBD_ID:1, Constants.BeepServerConstants.FRIEND_BBD_ID:2}),'application/json')
        self.assertEqual(response.status_code,200)
