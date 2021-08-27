from flask import Flask#从flask包中导入Flask类
from config import Config

# 数据库所需包
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 导入Flask-login扩展包
from flask_login import LoginManager

app = Flask(__name__, template_folder='../templates')#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
app.config.from_object(Config)

# 数据库对象
db = SQLAlchemy(app)
# 迁移引擎对象
migrate = Migrate(app, db)

login = LoginManager(app)

#print('等会谁（哪个包或模块）在使用我：',__name__)
from app import routes, models

# 注：上面两个app是完全不同的东西。两者都是纯粹约定俗成的命名，可重命名其他内容