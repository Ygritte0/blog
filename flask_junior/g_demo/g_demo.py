# encodig: utf-8

from flask import Flask, g, render_template, request
from utils import login_log

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhaomeng' and password == '1':
            # 就认为当前这个用户的用户名和密码正确
            g.username = 'zhaomeng'
            g.ip = 'xx'
            login_log()
            return '恭喜，登录成功'
        else:
            return u'您的用户名和密码错误！'


if __name__ == '__main__':
    app.run(debug=True)
