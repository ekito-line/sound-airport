# ローカル環境で動かすとき
Postgress.appをインストールしてください。
DjangoGirls Extensionsを参考にしながら、以下のデータベースを作成してください。
```
# CREATE USER admin;
# CREATE DATABASE soundsdb OWNER admin;
```
ローカルでサーバーを起動するときは、以下のコマンドを使用してください。
```
$ DJANGO_SETTINGS_MODULE=project.settings.local python manage.py runserver
```