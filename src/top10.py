import numpy as np
import pandas as pd
import streamlit as st
from .driver import connpass

st.header('connpass人気イベント')

events = connpass.GetEventData()

df = pd.DataFrame(
   np.random.randn(10, 6),
   columns=['title','started_at','ended_at','limit','accepted','event_url'],
   index=('TOP %d' % (i+1) for i in range(10)))

st.table(df)