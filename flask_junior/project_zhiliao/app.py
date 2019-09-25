# encodig: utf-8

from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
import config
from models import User, Question, Answer
from exts import db
from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by(Question.create_time.desc()).all()
    }
    return render_template('index.html', **context)


# index = login_required(index) = wrapper
# index() = wrapper()

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone,
                                 User.password == password).first()
        if user:
            # 将登录信息保存到cookie的session中
            session['user_id'] = user.id
            # 如果想在31天内都不需要重新登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            # 登录信息不正确的情况，要么是手机号错，要么是密码错，或者都错了
            return u'手机号或密码错误，请确认后再登录'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 获取数据并保存
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # 1. 如果手机号在数据库中已经存在，就不能再注册了
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return u'该手机号已被注册，请更换手机号码！'
        else:
            # 2. 验证password1和password2是一样的
            if password1 != password2:
                return u'两次密码不相等，请核对后再次填写！'
            else:
                user = User(telephone=telephone, username=username,
                            password=password1)
                db.session.add(user)
                db.session.commit()
                # 如果注册成功，就跳转到登录页面
                return redirect(url_for('login'))


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


@app.route('/logout/')
# 如何实现注销功能，
# 参考如何判断登录状态的，通过user_id,那么注销只要把user_id删掉就好了
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for('login'))


@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detail/<question_id>')
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question_model)


@app.route('/add_answer/ ', methods=['GET', 'POST'])
@login_required
def add_answer():
    content = request.form.get('answer_content')
    print('conent:', content)
    question_id = request.form.get('question_id')
    answer = Answer(content=content)
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    answer.author = user
    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


if __name__ == '__main__':
    app.run(debug=True)
