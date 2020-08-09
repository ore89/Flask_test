from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#appインスタンスの設定､flask_blogパッケージのconfigからインポートする
app.config.from_object("flask_blog.config")

#変数dbにデータベース(へのアクセス)を格納､dbを使用してデータべースが扱える
db = SQLAlchemy(app)

from flask_blog.views import entries, views
