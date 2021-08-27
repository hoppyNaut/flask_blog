from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm
from app import app#从app包中导入 app这个实例

from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user

#2个路由
@app.route('/')
@app.route('/index')
#1个视图函数
def index():
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template("index.html", posts=posts)#返回一个字符串

@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))
	return render_template("login.html", title='Sign In', form = form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))