import setup
setup.AddModulePath()

from datetime import datetime, timedelta
from typing import List, Dict
from driver import connpass
from mock.connpassAPI import *
from unittest import TestCase, mock
import unittest

class TestConnpass(TestCase):
    
    def test_GetTargetDate(self):
        """[summary]
        GetTargetDateのテストメソッド
        テストのためにdatetime.nowの日付を2022/09/17で固定する
        """
        datetime.now().replace(year=2022, month=9, day=17, hour=0, minute=0, second=0, microsecond=0)
        
        for addDay in range(7):
            actualDate = connpass.GetTargetDate(addDay)
            expectDate = datetime.now()
            
            if addDay > 0:
                expectDate = expectDate + timedelta(days=addDay)
                
            self.assertEqual(expectDate.strftime('%Y/%m/%d'), actualDate.strftime('%Y/%m/%d'))
    
    @mock.patch("driver.connpass.CallConnpassAPI")
    def test_CallConnpassAPI(self, mockCallConnpassAPI):
        mockCallConnpassAPI.return_value = readDummyData()
        result = connpass.CallConnpassAPI()
        self.assertEqual(369, len(result['events']))

    @mock.patch("driver.connpass.CallConnpassAPI")
    def test_GetEventData(self, mockCallConnpassAPI):
        mockCallConnpassAPI.return_value = readDummyData()
        headers = [
            { 'column_name': 'title', 'header_name': 'イベント名' },
            { 'column_name': 'accepted', 'header_name': '参加数' },
            { 'column_name': 'event_url', 'header_name': 'リンク' },
        ]
        # rankなし
        except_rank: int = 10
        result = connpass.GetEventData(headers)
        self.assertEqual(except_rank, len(result))
        # rankあり
        except_rank = 5
        result = connpass.GetEventData(headers, except_rank)
        self.assertEqual(except_rank, len(result))

if __name__ == "__main__":
    unittest.main()