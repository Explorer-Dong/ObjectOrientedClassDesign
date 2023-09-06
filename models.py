from exts import db


class Course(db.Model):
    __tablename__ = "course"
    number = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(20))
    college = db.Column(db.String(20))
    teacher = db.Column(db.String(15))


class Score(db.Model):
    __tablename__ = "score"
    number = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(10), nullable=True)
    chinese = db.Column(db.Integer, nullable=True)
    math = db.Column(db.Integer, nullable=True)
    english = db.Column(db.Integer, nullable=True)


class Student(db.Model):
    __tablename__ = "student"
    number = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    college = db.Column(db.String(10))
    major = db.Column(db.String(10))


# 邮箱 | 验证码进行相互绑定
class EmailVerification(db.Model):
    __tablename__ = "email_verification"
    number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    verification = db.Column(db.String(10), nullable=False)