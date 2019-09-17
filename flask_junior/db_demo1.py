from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(config)
print(app.config)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World'


