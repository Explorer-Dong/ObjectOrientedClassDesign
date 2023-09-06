from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import redirect

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


@app.route("/course/", methods=["GET", "POST"])
def course():
    if request.method == "GET":
        courses = Course.query.all()
        return render_template("course.html", courses=courses)
    else:
        return render_template("course.html")


# 分数表：主页 + 搜索
@app.route("/score/", methods=["GET", "POST"])
def score():
    if request.method == "GET":
        scores = Score.query.all()
        return render_template("score.html", scores=scores)
    else:
        name_keyword = request.form.get("form_score")
        
        if name_keyword == "":
            return render_template("score.html", name_keyword=name_keyword)
        else:
            scores = Score.query.filter(Score.name.like("%" + name_keyword + "%")).all()
            return render_template("score.html", name_keyword=name_keyword, scores=scores)
        

# 分数表：增加
@app.route("/score-add/", methods=["GET", "POST"])
def score_add():
    if request.method == "GET":
        return render_template("score-add.html")
    else:
        number = request.form.get("number")
        name = request.form.get("name")
        chinese = request.form.get("chinese")
        math = request.form.get("math")
        english = request.form.get("english")
        score = Score(number=number, name=name, chinese=chinese, math=math, english=english)
        db.session.add(score)
        db.session.commit()
        return redirect("/score")


# 分数表：删除，传入的参数是学号
@app.route("/score-delete/<string:score_number>", methods=["GET", "POST"])
def score_delete(score_number):
    if request.method == "POST":
        if request.form.get("confirmed") == "true":
            score = Score.query.filter(Score.number == score_number).first()
            db.session.delete(score)
            db.session.commit()
    return redirect("/score")


# 分数表：修改，传入的参数是学号
@app.route("/score-correct/<string:score_number>", methods=["GET", "POST"])
def score_correct(score_number):
    if request.method == "GET":
        return render_template("score-correct.html")
    else:
        score = Score.query.filter(Score.number == score_number).first()

        new_name = request.form.get("name")
        new_chinese = request.form.get("chinese")
        new_math = request.form.get("math")
        new_english = request.form.get("english")

        score.name = new_name
        score.chinese = new_chinese
        score.math = new_math
        score.english = new_english

        db.session.commit()
        return redirect("/score")


@app.route("/student/", methods=["GET", "POST"])
def student():
    if request.method == "GET":
        students = Student.query.all()
        return render_template("student.html", students=students)
    else:
        return render_template("student.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
