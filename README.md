# EventAnalysis

イベント分析

# 環境

Dockerで環境を構成している
下記のコマンドでdocker imageを作成して起動する

```sh
docker build -t eventanalysis . --no-cache
docker container run --name eventanalysis -it eventanalysis:latest
```


https://dash.plotly.com/