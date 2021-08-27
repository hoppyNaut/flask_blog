from datetime import datetime
# 加密密码
from werkzeug.security import generate_password_hash, check_password_hash
# 适用于大多数用户模型类的通用实现
from flask_login import UserMixin

from app import db, login

# @login.user_loader装饰器向Flask-Login注册用户加载函数。Flask-Login传递给函数的id作为一个参数将是一个字符串，所以需要将字符串类型转换为int型以供数据库使用数字ID
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post {}'.format(self.body)
