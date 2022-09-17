from datetime import datetime,timedelta
from typing import List, Dict
import requests

columns = ["event_id","title","started_at","ended_at","updated_at","limit","accepted","waiting","event_url"]
isTrace: bool = False

def GetTargetDate(days: int = 0) -> datetime:
    """[summary]
    抽出日を返す
    Args:
        days (int): 加算日
    Returns:
        (datetime): 抽出日
    """
    targetdate = datetime.today()
    if days == 0:
        return targetdate
    
    targetdate = targetdate + timedelta(days=days)
    return targetdate

def CallConnpassAPI(targetdate: datetime, startindex: int = 1) -> Dict:
    """[summary]
    ConnpassAPIを実行し、実行結果をJSONで取得する
    Args:
        eventdate (str): 開催日
        startindex (int): 開始位置 デフォルト1
    Returns:
        (dict): 実行結果
    """
    url = "https://connpass.com/api/v1/event/"
    params = {
        'ymd': targetdate.strftime('%Y/%m/%d'),
        'count': 100,
        'start': startindex,
        'order': 2
    }

    try:
        responce = requests.get(url, params=params)
        result_json = responce.json()
        return result_json
    except Exception as e:
        print('Error code: ', e.code)
        raise e

def FilterEvents(targetdate: datetime, events: List) -> List:
    """[summary]
    イベントデータリストより開催日時や終了日時が抽出日と一致するイベントデータを取得する
    Args:
        targetdate (datetime)   : 抽出日
        events (List)           : イベントデータリスト
    Returns:
        (List): イベントデータ(JSON形式)
    """
    eventList = []
    targetdateString: str = targetdate.strftime('%Y-%m-%d')
    for event in events:
        started_at: str = event["started_at"]
        ended_at: str = event["ended_at"]
        if started_at.startswith(targetdateString) or ended_at.startswith(targetdateString):
            eventList.append(event)
    return eventList

def GetEventData() -> List:
    """[summary]
    イベントデータを取得する
    Args:
        isDebug (bool): DEBUG出力するかどうか
    Returns:
        (List): イベントデータ(JSON形式)
    """
    result = []
    for addDay in range(7):
        targetdate = GetTargetDate(addDay)
        eventData = CallConnpassAPI(targetdate)
        appendList = FilterEvents(targetdate, eventData['events'])
        if appendList.count > 0:
            result.extend(appendList)
        results_start: int = int(eventData["results_start"])
        results_available: int = int(eventData["results_available"])
        results_returned: int = int(eventData["results_returned"])
        
        while results_returned == 100 and results_available > 100:
            results_start += 100
            eventData = CallConnpassAPI(targetdate, results_start)
            results_start: int = int(eventData["results_start"])
            results_available: int = int(eventData["results_available"])
            results_returned: int = int(eventData["results_returned"])
            appendList = FilterEvents(targetdate, eventData['events'])
            if appendList.count > 0:
                result.extend(appendList)
        
    return result

if __name__ == '__main__':
    isTrace = True
    result = CallConnpassAPI(datetime.today(), 1)
    print(result)