from flask import Flask, session
import os
from datetime import timedelta

app = Flask(__name__)
# '24个字符的字符串'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


# 添加数据到session中，
# 操作session和操作字典一样
# SECRET_KEY

@app.route('/')
def index():
    session['name'] = 'zhaomeng'
    # 如果未指定session的过期时间，默认过期时间为浏览器关闭时
    # 如果设置session的permanent属性为TRUE，则过期时间为31天
    session.permanent = True
    return 'index'


@app.route('/get/')
def get():
    # session['name'] 当'name'这个键不存在的时候，会报出异常
    # session.get('name') 当'name'这个键不存在的时候，会返回一个None.更推荐使用
    return session.get('name')


@app.route('/delete/')
def delete():
    print(session.get('name'))
    session.pop('name')
    print(session.get('name'))
    return 'success'


@app.route('/clear')
def clear():
    # 删除session中的所有数据
    print(session.get('name'))
    session.clear()
    print(session.get('name'))
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
