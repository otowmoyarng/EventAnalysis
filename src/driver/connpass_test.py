from asyncore import loop
import connpass
from datetime import datetime, timedelta
from typing import List, Dict
import unittest

class ConnpassTest(unittest.TestCase):
    
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
    
    def test_CallConnpassAPI(self):
        def traceEventData(events: Dict, targetDate: datetime, startindex: int = 1):
            print(f"targetDate:{targetDate.strftime('%Y/%m/%d')}, startindex:{str(startindex)}")
            columns = ["event_id","title","started_at","ended_at","updated_at","limit","accepted","waiting","event_url"]
            
            headerText = ''
            for column in columns:
                if headerText != '':
                    headerText += ","
                headerText += column
            print(headerText)
                 
            loopCount: int = 0
            for event in events["events"]:
                if loopCount >= 4:
                    break
                
                recordText = ''
                for column in columns:
                    if recordText != '':
                        recordText += ","
                    
                    if isinstance(event[column], str):
                        recordText += event[column]
                    else:
                        recordText += str(event[column])
                print(recordText)
                loopCount += 1
        
        # 処理日で実行する
        startindex: int = 1
        targetDate: datetime = datetime.now()
        traceEventData(connpass.CallConnpassAPI(targetDate), targetDate)
        
        # 処理日で実行する
        startindex += 100
        traceEventData(connpass.CallConnpassAPI(targetDate), targetDate, startindex)
        traceEventData(connpass.CallConnpassAPI(targetDate, startindex), targetDate)
        
        # 処理日の翌日で実行する
        targetDate = targetDate + timedelta(days=1)
        traceEventData(connpass.CallConnpassAPI(targetDate), targetDate)

    def test_FilterEvents(self):
        targetDate: datetime = datetime.now()
        eventData = connpass.CallConnpassAPI(targetDate)
        appendList = connpass.FilterEvents(targetDate, eventData['events'])
        
        targetdateString: str = targetDate.strftime('%Y-%m-%d')
        for item in appendList:
            started_at: str = item["started_at"]
            ended_at: str = item["ended_at"]
            actual = started_at.startswith(targetdateString) or ended_at.startswith(targetdateString)
            self.assertTrue(actual, f"targetdateString:{targetdateString}, started_at:{started_at}, ended_at:{ended_at}")

if __name__ == "__main__":
    unittest.main()