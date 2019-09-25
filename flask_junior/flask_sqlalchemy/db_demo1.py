from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(config)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


db.create_all()


@app.route('/')
def hello_world():
    # # 增加
    # article1 = Article(title='byx', content='criminal')
    # db.session.add(article1)
    # # 事务
    # db.session.commit()
    # 查
    # select * from article where title='byx';
    # result = Article.query.filter(Article.title == 'byx')
    # print(result)
    # article1 = result[0]
    # print(article1.title)
    # print(article1.content)
    # # 改
    # # 1. 先把你要更改的数据查找出来
    # article1 = Article.query.filter(Article.title == 'byx').first()
    # # 2. 把这条数据需要修改的地方进行修改
    # article1.title = 'new title'
    # # 3. 做事务的提交
    # db.session.commit()
    # 删
    # 1. 把要删的先查找出来
    articel = Article.query.filter(Article.title == 'new title').first()
    # 2. 删除
    db.session.delete(articel)
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
