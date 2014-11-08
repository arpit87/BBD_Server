from django.test import TestCase
from Chat import Constants
import json
import Platform.Constants

# Create your tests here.
class ChatRESTtest(TestCase):
    def test_createChatUserTest(self):
        inputval = json.dumps({Constants.ChatServerConstants.CHATUSERNAME:"user1005",
                            Constants.ChatServerConstants.CHATPASSWORD:"rrrr"})
        response = self.client.post('/Chat/createChatUser/',inputval,Platform.Constants.RESPONSE_JSON_TYPE)
        self.assertEqual(response.status_code,200)
