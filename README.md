# EventAnalysis

イベント分析

# 環境

Dockerで環境を構成している
image:eventanalysis

```sh
docker build -t eventanalysis .
docker container run --name eventanalysis -it eventanalysis:latest
```

```dockerfile
FROM python:3.9.8

WORKDIR /usr/src/EventAnalysis

COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/* ./
COPY README.md ./
```


仮想環境venvにて構成している。
仮想環境の作成方法はこれ

```shell
python -m venv EventAnalysis
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

仮想環境を起動する場合は`source EventAnalysis/bin/activate`を実行する。
終了するには`deactivate`を実行する。
windowsの場合は`.\EventAnalysis\Scripts\activate.bat`を実行する。
終了するには`.\EventAnalysis\Scripts\deactivate.bat`を実行する。

https://dash.plotly.com/