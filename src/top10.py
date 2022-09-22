import numpy as np
import pandas as pd
import streamlit as st
from driver import connpass

# 初期化
st.set_page_config(
    page_title="connpass人気イベント",
    layout="wide")

st.header('connpass人気イベント')

# イベントデータ
headers = [
    { 'column_name': 'title', 'header_name': 'イベント名' },
    { 'column_name': 'accepted', 'header_name': '参加数' },
    { 'column_name': 'event_url', 'header_name': 'リンク' },
]
events = connpass.GetEventData(headers)

df = pd.DataFrame(
    events,
    columns=['イベント名','参加数','リンク'],
    index=('%d' % (i+1) for i in range(10))
)
st.table(data=df)