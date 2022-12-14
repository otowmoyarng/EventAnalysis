from datetime import datetime,timedelta
from typing import List, Dict
import copy
import requests

columns = ["event_id","title","started_at","ended_at","updated_at","limit","accepted","waiting","event_url"]

def GetTargetDate(days: int = 0) -> datetime:
    """[summary]
    抽出日を返す
    Args:
        days (int): 加算日 デフォルト0
    Returns:
        (datetime): 抽出日
    """
    targetdate = datetime.today()
    if days == 0:
        return targetdate
    
    targetdate = targetdate + timedelta(days=days)
    return targetdate

def CallConnpassAPI(startindex: int = 1) -> Dict:
    """[summary]
    ConnpassAPIを実行し、実行結果をJSONで取得する
    Args:
        startindex (int): 開始位置 デフォルト1
    Returns:
        (dict): 実行結果
    """
    url = "https://connpass.com/api/v1/event/"
    dates: str = ''
    for addDay in range(7):
        targetdate = GetTargetDate(addDay)
        if len(dates) > 0:
            dates += ','
        dates += targetdate.strftime('%Y%m%d')
    params = {
        'ymd': dates,
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

def GetEventData(headers: List, rank: int = 10) -> List:
    """[summary]
    イベントデータを取得する
    Args:
        rank (int): ランキング順位 デフォルト10
    Returns:
        (List): イベントデータ(JSON形式)
    """
    # connpassからイベントデータを抽出する
    events = []
    eventData = CallConnpassAPI()
    results_start: int = int(eventData["results_start"])
    results_available: int = int(eventData["results_available"])
    results_returned: int = int(eventData["results_returned"])
    if len(eventData['events']):
        events.extend(eventData['events'])
    
    while results_returned == 100 and results_available > 100:
        results_start += 100
        eventData = CallConnpassAPI(results_start)
        results_start: int = int(eventData["results_start"])
        results_available: int = int(eventData["results_available"])
        results_returned: int = int(eventData["results_returned"])

        if len(eventData['events']):
            events.extend(eventData['events'])
    
    # 参加者数でソートしてTOP10を抽出する
    sortlist = sorted(copy.deepcopy(events), key=lambda x: -x['accepted'])
    if len(sortlist) > rank:
        sortlist = sortlist[:rank]

    # 表示データの成型
    result = []
    for event in sortlist:
        tablerow = {}
        for header in headers:
            column_name: str = header['column_name']
            header_name: str = header['header_name']
            tablerow[header_name] = event[column_name]
        result.append(tablerow)
    return result