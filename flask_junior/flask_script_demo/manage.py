# encoding: utf-8

from flask_script import Manager
from flask_script_demo import app
from db_scripts import DBmanager

manager = Manager(app)


# 和数据库相关的操作都放在一起

@manager.command
def runserver():
    print('服务器跑起来了!!!')


# 把db_scripts中的命令引用过来
# python manage.py db init
# python manage.py db migrate
manager.add_command('db', DBmanager)

if __name__ == '__main__':
    manager.run()
