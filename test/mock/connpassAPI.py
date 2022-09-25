import json
from typing import Dict

def readDummyData() -> Dict:
    """
    モック用データを読み込む
    """
    result = {}
    with open('mock/connpass_Dummy.json', encoding="utf-8") as f:
        result = json.load(f)
    return result
        