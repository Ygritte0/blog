from flask_script import Manager
from migrate_demo import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
from models import Article

# init  初始化迁移的环境， 只有在第一次创建迁移的时候使用该命令，再创建迁移就不用再初始化环境了
# migrate 生成迁移文件
# upgrade 将迁移映射到表中
# 模型——> 迁移文件 ——> 表

manager = Manager(app)

# 1. 要使用flask_migrate，必须绑定app和db
migrate = Migrate(app, db)

# 2. 把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
