import unittest
from models import facebook_services
from facebook_business.api import FacebookAdsApi
import json

class TestGetAds(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app_id = '677752197796360'
        app_secret = 'b4ddf1dd78d1fd88ee6d251f47dfd11e'
        access_token = 'EAAJoaXrZB0ggBO2xgy27MiVazt0XHj4h3NCboAdoCpC8CnGdVZACXSwUxDo0IfPUEU02ZCphBU5I2JMF4qXBZByt6A8iZAD0mhVc9LWdrZAQZAPkos8ZBvr97LUZAP5SOFPExQZAO4SYwDItRYlVOmYiNqIL9TdZC0KgZAeOoYekNnQRTAaxXLH8AZA1hFN4KBxVJB0UR'
        FacebookAdsApi.init(app_id, app_secret, access_token)

    def test_get_ads(self):
        adset_id = 'act_104028533759661'  # Substitua pelo ID do conjunto de anúncios
        ads = facebook_services.get_ads(adset_id)
        ads_json = json.dumps(ads, indent=4)  # Convertendo para JSON
        print("Ads:", ads_json)
        self.assertIsNotNone(ads)
        self.assertIsInstance(ads, list)

if __name__ == '__main__':
    unittest.main()
