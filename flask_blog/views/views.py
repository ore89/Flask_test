from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps

'''
※entrues.pyに移動

#このURLがリクエストされたとき
@app.route("/")
#以下のメソッドが呼び出される
def show_entries():
    #sessionの"logged_in"がFalseなら(ログインしてないなら)､先頭ページに移動
    if not session.get("logged_in"):
        #url_forでアドレスを指定せず､routeの関数を直接呼び出し
        return redirect(url_for("login"))
    return render_template("entries/index.html")
'''

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return inner

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    #ログインページからpostされると､このif節が使われる
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            flash("ユーザ名が異なります")
        elif request.form["password"] != app.config["PASSWORD"]:
            flash("パスワードが異なります")
        else:
            #ここでログイン
            #ここでsession変数をTrueに変更し､以降このパラメータでログインを判断
            session["logged_in"] = True
            flash("ログインしました")
            return redirect(url_for("show_entries"))
    #最初はpostが無いのでここに来てlogin.htmlを表示
    return render_template("login.html")

@app.route("/logout")
def logout():
    #ログアウトする場合は､session変数の"logged_in"を削除する
    session.pop("logged_in", None)
    flash("ログアウトしました")
    return redirect(url_for("show_entries"))

@app.route("/test")
def show_test():
    return render_template("entries/test.html")
