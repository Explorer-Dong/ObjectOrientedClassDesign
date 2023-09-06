from flask import Blueprint, request, render_template, redirect
from exts import db
from models import Student


bp = Blueprint("student", __name__, url_prefix="/")


# 学生表：主页 + 搜索
@bp.route("/student/", methods=["GET", "POST"])
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
@bp.route("/student-add/", methods=["GET", "POST"])
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
@bp.route("/student-delete/<string:student_number>", methods=["GET", "POST"])
def student_delete(student_number):
    if request.method == "POST":
        if request.form.get("confirmed") == "true":
            student = Student.query.filter(Student.number == student_number).first()
            db.session.delete(student)
            db.session.commit()
    return redirect("/student")


# 学生表：修改，传入的参数是学号
@bp.route("/student-correct/<string:student_number>", methods=["GET", "POST"])
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
