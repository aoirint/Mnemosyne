# Mnemosyne
3Dプリンタに使うフィラメントの在庫と使用量を記録するためのWebアプリ。

![new filament](https://i.imgur.com/DEFL6mg.png)

![new 3dprint](https://i.imgur.com/EtG8CH2.png)

`docker-compose.yaml`をこのリポジトリからコピーし、SECRETなどを適切に書き換えたのち、以下のように起動する。

```bash
docker-compose pull
docker-compose up -d
# Or
make pull
make up
```

## Development

Create `docker-compose.override.yaml`.

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
