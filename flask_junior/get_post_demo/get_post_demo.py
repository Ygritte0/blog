from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/')
def search():
    # arguments, 是一个字典
    q = request.args.get('q')
    return u'用户提交的查询参数是： %s' % q


# 默认的视图函数，只能采用get请求
# 如果要用post请求，要写明
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        request.form.get('username')
        request.form.get('password')
        return 'post request'


if __name__ == '__main__':
    app.run(debug=True)
