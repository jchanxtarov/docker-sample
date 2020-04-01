FROM python:3.7.5

ARG app_dir=/src/

ADD requirements.txt $app_dir

WORKDIR $app_dir

# RUN pip install --upgrade pip

# 利用するパッケージがかたまるまでコメントアウトしてても良さそう
RUN pip install -r requirements.txt

# migrationコマンドとかをshに登録して実行できるようにしたい
# RUN sh /etc/init.sh