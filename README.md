# EventAnalysis

イベント分析

# 環境

Dockerで環境を構成している
下記のコマンドでdocker imageを作成して起動する

```sh
docker build -t eventanalysis . --no-cache
docker container run --name eventanalysis -it eventanalysis:latest
```

# 本番環境
masterブランチにpushするとhttps://streamlit.io/cloudにデプロイされる
https://otowmoyarng-eventanalysis-srctop10-0qfuoc.streamlitapp.com/