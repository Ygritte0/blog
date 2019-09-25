from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

# SQLalchemy实例化，需要读取app.config中数据库相关的配置；
# 所以要先加载配置，然后再实例化数据库

app.config.from_object(config)
db = SQLAlchemy(app)

# # 用户表
# create_table_users(
#     id int primary key autoincrement,
#     username varchar(100) not null
# )
# # 文章表
# create_table_article(
# id int primary key autoincrement,
# title varchar(100) not null,
# content text not null,
# author_id int,
# foreign key 'author_id' references 'users.id'
# )

# 根据以上语句写模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer,
                          db.ForeignKey('user.id'))  # 此处的'user'是表名，不是模型
    author = db.relationship('User', backref=db.backref('articles'))


db.create_all()


@app.route('/')
def index():
    # 添加一篇文章，又因为文章必须依赖用户而存在，所以需要先添加用户
    # user1 = User(username='zm')
    # db.session.add(user1)
    # db.session.commit()

    # articel = Article(title='byx', content='criminal', author_id=1)
    # db.session.add(articel)
    # db.session.commit()

    # 我要找文章标题为byx的作者
    # article = Article.query.filter(Article.title == 'byx').first()
    # author_id = article.author_id
    # user = User.query.filter(User.id == author_id).first()
    # print("username: %s" % user.username)

    # article.author
    # author = User.query.filter(User.username=='zm').first()
    # author.articles

    article = Article.query.filter(Article.title == 'byx').first()
    article.author = User.query.filter(User.id == 1).first()
    db.session.add(article)
    db.session.commit()
    print('username: %s' % article.author.username)

    # # 我要找zm用户写的所有文章
    # article = Article(title='homels', content='detective', author_id=1)
    # db.session.add(article)
    # db.session.commit()
    # user = User.query.filter(User.username == 'zm').first()
    # result = user.articles
    # for article in result:
    #     print('='*10)
    #     print(article.title)

    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
