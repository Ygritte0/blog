DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '12345'
# 密码可以在mysql-init.txt中设置：
# ALTER USER 'root'@'localhost' IDENTIFIED BY '12345';
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'migrate_demo'  # 你这里连的是demo3的数据库，所以是从demo3里面找的


# 依据第一条注释的格式来设置
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,
                                                                       DRIVER,
                                                                       USERNAME,
                                                                       PASSWORD,
                                                                       HOSTNAME,
                                                                       PORT,
                                                                       DATABASE)

# SQLALCHEMY_DATABASE_URI = 'mysql://root:12345@127.0.0.1/db_demo1'

SQLALCHEMY_TRACK_MODIFICATIONS = True