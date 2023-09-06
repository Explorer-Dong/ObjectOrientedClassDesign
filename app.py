from flask import Flask, request, render_template, redirect
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


@app.route("/")
def index():
    return render_template("index.html")


# 课程表：主页 + 搜索
@app.route("/course/", methods=["GET", "POST"])
def course():
    if request.method == "GET":
        courses = Course.query.all()
        return render_template("course.html", courses=courses)
    else:
        course_keyword = request.form.get("form_course")
        
        if course_keyword == "":
            return render_template("course.html", course_keyword=course_keyword)
        else:
            courses = Course.query.filter(Course.course_name.like("%" + course_keyword + "%")).all()
            return render_template("course.html", course_keyword=course_keyword, courses=courses)


# 课程表：增加
@app.route("/course-add/", methods=["GET", "POST"])
def course_add():
    if request.method == "GET":
        return render_template("course-add.html")
    else:
        course_order = request.form.get("course_order")
        course_name = request.form.get("course_name")
        college = request.form.get("college")
        teacher = request.form.get("teacher")
        course = Course(course_order=course_order, course_name=course_name, college=college, teacher=teacher)
        db.session.add(course)
        db.session.commit()
        return redirect("/course")
    

# 课程表：删除，传入的参数是课程号
@app.route("/course-delete/<string:course_order>", methods=["GET", "POST"])
def course_delete(course_order):
    if request.method == "POST":
        if request.form.get("confirmed") == "true":
            course = Course.query.filter(Course.course_order == course_order).first()
            db.session.delete(course)
            db.session.commit()
    return redirect("/course")


# 课程表：修改，传入的参数是课程号
@app.route("/course-correct/<string:course_order>", methods=["GET", "POST"])
def course_correct(course_order):
    if request.method == "GET":
        return render_template("course-correct.html")
    else:
        course = Course.query.filter(Course.course_order == course_order).first()

        new_course_name = request.form.get("course_name")
        new_college = request.form.get("college")
        new_teacher = request.form.get("teacher")

        course.course_name = new_course_name
        course.college = new_college
        course.teacher = new_teacher

        db.session.commit()
        return redirect("/course")
    

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


# 学生表：主页 + 搜索
@app.route("/student/", methods=["GET", "POST"])
def student():
    if request.method == "GET":
        students = Student.query.all()
        return render_template("student.html", students=students)
    else:
        name_keyword = request.form.get("form_student")
        
        if name_keyword == "":
            return render_template("student.html", name_keyword=name_keyword)
        else:
            students = Student.query.filter(Student.name.like("%" + name_keyword + "%")).all()
            return render_template("student.html", name_keyword=name_keyword, students=students)


# 学生表：增加
@app.route("/student-add/", methods=["GET", "POST"])
def student_add():
    if request.method == "GET":
        return render_template("student-add.html")
    else:
        number = request.form.get("number")
        name = request.form.get("name")
        age = request.form.get("age")
        college = request.form.get("college")
        major = request.form.get("major")
        student = Student(number=number, name=name, age=age, college=college, major=major)
        db.session.add(student)
        db.session.commit()
        return redirect("/student")
    

# 学生表：删除，传入的参数是学号
@app.route("/student-delete/<string:student_number>", methods=["GET", "POST"])
def student_delete(student_number):
    if request.method == "POST":
        if request.form.get("confirmed") == "true":
            student = Student.query.filter(Student.number == student_number).first()
            db.session.delete(student)
            db.session.commit()
    return redirect("/student")


# 学生表：修改，传入的参数是学号
@app.route("/student-correct/<string:student_number>", methods=["GET", "POST"])
def student_correct(student_number):
    if request.method == "GET":
        return render_template("student-correct.html")
    else:
        student = Student.query.filter(Student.number == student_number).first()

        new_name = request.form.get("name")
        new_age = request.form.get("age")
        new_college = request.form.get("college")
        new_major = request.form.get("major")

        student.name = new_name
        student.age = new_age
        student.college = new_college
        student.major = new_major

        db.session.commit()
        return redirect("/student")


if __name__ == "__main__":
    app.run(debug=True)
