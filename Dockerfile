# ベースイメージの取得
FROM ubuntu:20.04

WORKDIR /usr/src

# メタデータの登録
LABEL version="1.0"
LABEL description="EventAnalysisの開発検証環境"

# 必要パッケージのインストール
RUN apt update
RUN apt upgrade -y

# githubからクローン
RUN apt install -y git
RUN mkdir EventAnalysis
RUN git clone https://github.com/otowmoyarng/EventAnalysis.git EventAnalysis/

# python準備
RUN apt install -y python3 
RUN apt install -y python3-pip 
RUN pip3 install -r EventAnalysis/requirements.txt

# 最後におまじない[apt update]を実行する
RUN apt update
