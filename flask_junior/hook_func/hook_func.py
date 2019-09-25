# encodig: utf-8
import datetime
import os
from flask import Flask, render_template, request, session, redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello_world():
    print('index')
    return render_template('index.html')


# before_request:在请求之前执行
# before_request是在所有视图函数执行之前执行的
# 这个函数只是一个装饰器，它能把需要设置为钩子函数的代码放到视图函数执行之前执行

@app.before_request
def my_before_request():
    if session.get('username'):
        g.username = session.get('username')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    print('login')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhaomeng' and password == '1':
            session['username'] = 'zhaomeng'
            return u'登录成功'
        else:
            return u'用户名或密码错误'


@app.route('/edit/')
def edit():
    # if hasattr(g, 'username'):
    #     return u'修改成功'
    # else:
    #     return redirect(url_for('login'))
    return render_template('edit.html')


@app.context_processor
def my_context_processor():
    """app.context_processor的作用是返回一个字典，
    flask会遍历这个字典里所有的key，使它在模板（我不知道有没有别的应用场景）里可用
    比如这个例子中，反回了username，那么在模板里就可以直接使用了。
    当做全局变量来用，不需要每个视图函数渲染的时候，传递参数了

    :return:
    """
    # username = session.get('username', 'no username')
    # return {'username': username}
    username = session.get('username')
    def now():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if username:
        # 如果没有username那么你这个函数会返回None，
        # 所以如果返回了None，那么flask遍历时就会报错了，
        # 修改办法就是让他使用有一个可迭代的返回值
        return {'username': username, 'now': now}
    return {'now': now}  # 可以返回一个空字典，也可以给username一个默认值，都可以

if __name__ == '__main__':
    app.run(debug=True)
