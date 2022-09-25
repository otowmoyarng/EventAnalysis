# EventAnalysis

イベント分析

# 環境

Dockerで環境を構成している
下記のコマンドでdocker imageを作成して起動する

```sh
docker build -t eventanalysis . --no-cache
docker container run --name eventanalysis -it eventanalysis:latest
```

src配下にて下記コマンドを実行するとlocalhost:8501でブラウザが起動する

```sh
streamlit run top10.py
```

# streamlit環境

https://otowmoyarng-eventanalysis-srctop10-0qfuoc.streamlitapp.com/

masterブランチにpushするとhttps://streamlit.io/cloudにデプロイされる

# streamlitについて

https://streamlit.io/

サンプルコード

```python
import numpy as np
import pandas as pd
import streamlit as st

st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)
```