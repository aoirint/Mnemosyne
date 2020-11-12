# Mnemosyne
3Dプリンタに使うフィラメントの在庫と使用量を記録するためのWebアプリ。

Docker仮対応中（nginxによる静的ファイル配信対応）。

デプロイ時はgunicornによる起動に書き換えてください（nginx対応と同時に対応予定）。

## ビルド
```
docker build . -t aoirint/Mnemosyne
```

## 実行（開発用）
```
docker run --rm -it -p 8000:8000 -e DJANGO_SECRET=hogehoge -e ALLOWED_HOST=* -e ENVIRONMENT=development aoirint/mnemosyne
```

ホストの`0.0.0.0:8000`にフォワーディングします。
デフォルトのDockerfileのコマンドは開発用簡易サーバなので注意。
