from flask import Blueprint, request
from exts import mail, db
from flask_mail import Message
import string, random
from models import EmailVerification


bp = Blueprint("auth", __name__, url_prefix="/auth")


# 登录
@bp.route("/login")
def login():
	return "login"


# 注册
@bp.route("/register")
def register():
	return "register"


# 根据用户输入的邮箱进行动态的发送邮件验证码
@bp.route("/mail")
def send_email():
	# /auth/mail?email=explorer-dong@foxmail.com
	email = request.args.get("email")

	# 生成 6 位数验证码
	source = string.digits * 6
	verification = random.sample(source, 6)
	verification = "".join(verification)
	
	# 发送验证码到用户输入的邮件
	message = Message(subject='教务管理系统-验证码', recipients=[email], body=f'您的验证码是{verification}，请不要告诉请他人哦。')
	mail.send(message)

	# 将生成的验证码进行存储，最好的方式是进行缓存，但是为了降低难度就存入数据库
	email_verification = EmailVerification(email=email, verification=verification)
	db.session.add(email_verification)
	db.session.commit()

	return "send email successfully!"
