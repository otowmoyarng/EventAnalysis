import setup
setup.AddModulePath()

import unittest
from datetime import datetime, timedelta
from typing import List, Dict
from driver import connpass

class TestConnpass(unittest.TestCase):
    
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
        def traceEventData(events: Dict, startindex: int = 1):
            # print(f"startindex:{str(startindex)}")
            columns = ["event_id","title","started_at","ended_at","updated_at","limit","accepted","waiting","event_url"]
            
            headerText = ''
            for column in columns:
                if headerText != '':
                    headerText += ","
                headerText += column
            # print(headerText)
                 
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
                # print(recordText)
                loopCount += 1
        
        # 処理日で実行する
        startindex: int = 1
        traceEventData(connpass.CallConnpassAPI())
        
        # 処理日で実行する
        startindex += 100
        traceEventData(connpass.CallConnpassAPI(startindex), startindex)

    def test_GetEventData(self):
        pass

if __name__ == "__main__":
    unittest.main()