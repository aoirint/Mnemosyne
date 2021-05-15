# Mnemosyne
3Dプリンタに使うフィラメントの在庫と使用量を記録するためのWebアプリ。

![new filament](https://i.imgur.com/DEFL6mg.png)

![new 3dprint](https://i.imgur.com/EtG8CH2.png)


## Deploy
1. `docker-compose.yaml`をこのリポジトリからコピーする
2. `nginx`ディレクトリをこのリポジトリからコピーする
    - ディレクトリ構造
        - `docker-compose.yaml`
        - `nginx/`
            - `default.conf.template`
3. `DJANGO_SECRET_KEY`を書き換える
    - `pip3 install -U django && python3 -c "from django.core.management import utils; print(f'SECRET_KEY={utils.get_random_secret_key()}')"`
4. `make pull`（`docker-compose pull`）で最新のDockerイメージを取得する
5. `make up`（`docker-compose up -d`）で起動する
6. `make logs`（`docker-compose logs -f`）でログを確認する
7. リバースプロキシの設定をする
    - デフォルトで`127.0.0.1:8000`にバインド

- 停止：`make down`
- 全データの削除：`make dangerous-down`


## Development

`docker-compose.override.yaml`を作成する。

```yaml
version: '3.8'
services:
  app:
    build: ./app
    command: python3 /code/manage.py runserver 0.0.0.0:8000

    volumes:
      - ./app/django:/code

    environment:
      DJANGO_DEBUG: 1
```
