from flask_script import Command
from flask_blog import db

#スクリプト実行のクラスを定義､クラス名(Command):と入力することで､スクリプト実行のためのクラスとして定義
#
class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()
