from django.test import TestCase
from Trends.calc_trends import calc_trends
from Trends.Constants import TimeConstants,TrendServerConstants
from Trends.models import beeptimetrends
# Create your tests here.
class TrendsCalcTest(TestCase):
    fixtures = ["test_data.json"]
    def test_calc_trends(self):
        calc_trends(TimeConstants.DAILY)
        trends = beeptimetrends.objects.all()
        print trends.values()
        return

class GetTrendsTest(TestCase):
    fixtures = ["test_data.json"]
    def test_getDailyTimeTrends(self):
        input = dict({TrendServerConstants.TREND_TYPE:TimeConstants.DAILY,TrendServerConstants.TOP_NUM:6})
        response = self.client.get('/Trends/getTimeTrends/',input)
        self.assertEqual(response.status_code,200)
        print(response.content)

    def test_getWeeklyTimeTrends(self):
        input = dict({TrendServerConstants.TREND_TYPE:TimeConstants.WEEKLY,TrendServerConstants.TOP_NUM:6})
        response = self.client.get('/Trends/getTimeTrends/',input)
        self.assertEqual(response.status_code,200)
        print(response.content)

    def test_getMonthlyTimeTrends(self):
        input = dict({TrendServerConstants.TREND_TYPE:TimeConstants.MONTHLY,TrendServerConstants.TOP_NUM:6})
        response = self.client.get('/Trends/getTimeTrends/',input)
        self.assertEqual(response.status_code,200)
        print(response.content)