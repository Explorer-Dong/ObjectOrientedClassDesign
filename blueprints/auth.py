from flask import Blueprint, render_template
from exts import mail
from flask_mail import Message


bp = Blueprint("auth", __name__, url_prefix="/auth")


# 登录
@bp.route("/login")
def login():
	return "login"


# 注册
@bp.route("/register")
def register():
	return "register"


# 测试发送验证邮件
@bp.route("/mail")
def send_mail():
	message = Message(subject='邮箱发送测试', recipients=['explorer-dong@foxmail.com'], body='这是一封测试邮件')
	mail.send(message)
	return '邮件发送成功！'