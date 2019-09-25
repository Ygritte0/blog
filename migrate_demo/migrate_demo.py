from flask import Flask
from models import Article
from exts import db
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# with app.app_context():
#     db.create_all()


# 新建一个article模型，采用models分开的方式

@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
