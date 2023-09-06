from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/admin?charset=utf8mb4"

db = SQLAlchemy(app)


class Course(db.Model):
    __tablename__ = "course"
    course_order = db.Column(db.String(10), primary_key=True)
    course_name = db.Column(db.String(20))
    college = db.Column(db.String(20))
    teacher = db.Column(db.String(10))


class Score(db.Model):
    __tablename__ = "score"
    number = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(10))
    chinese = db.Column(db.Integer)
    math = db.Column(db.Integer)
    english = db.Column(db.Integer)


class Student(db.Model):
    __tablename__ = "student"
    number = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    college = db.Column(db.String(10))
    major = db.Column(db.String(10))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/course", methods=["GET", "POST"])
def course():
    if request.method == "GET":
        courses = Course.query.all()
        return render_template("course.html", courses=courses)
    else:
        return render_template("course.html")


@app.route("/score", methods=["GET", "POST"])
def score():
    if request.method == "GET":
        scores = Score.query.all()
        return render_template("score.html", scores=scores)
    else:
        return render_template("score.html")


@app.route("/student", methods=["GET", "POST"])
def student():
    if request.method == "GET":
        students = Student.query.all()
        return render_template("student.html", students=students)
    else:
        return render_template("student.html")


if __name__ == "__main__":
    app.run(debug=True)
