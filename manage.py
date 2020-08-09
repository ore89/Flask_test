from flask_script import Manager
from flask_blog import app

#scriptsフォルダ内のdb.pyのInitDBクラスをインストール
from flask_blog.script.db import InitDB

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command("init_db", InitDB())
    manager.run()
