dockerの勉強用のサンプル

```
$ docker-compose build
$ docker-compose up
```
```
# 全コンテナの削除
$ docker rm $(docker ps -q -a)

# 全イメージの削除の削除
$ docker rmi $(docker images -q)
```