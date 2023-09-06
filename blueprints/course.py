from flask import Blueprint, request, render_template, redirect
from exts import db
from models import Course


bp = Blueprint("course", __name__, url_prefix="/")


# 课程表：主页 + 搜索
@bp.route("/course/", methods=["GET", "POST"])
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
@bp.route("/course-add/", methods=["GET", "POST"])
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
        return redirect("/course/")
    

# 课程表：删除，传入的参数是课程号
@bp.route("/course-delete/<string:course_order>", methods=["GET", "POST"])
def course_delete(course_order):
    if request.method == "POST":
        if request.form.get("confirmed") == "true":
            course = Course.query.filter(Course.course_order == course_order).first()
            db.session.delete(course)
            db.session.commit()
    return redirect("/course/")


# 课程表：修改，传入的参数是课程号
@bp.route("/course-correct/<string:course_order>", methods=["GET", "POST"])
def course_correct(course_order):
    if request.method == "GET":
        return render_template("course-correct.html")
    else:
        old_course = Course.query.filter(Course.course_order == course_order).first()

        new_course_name = request.form.get("course_name")
        new_college = request.form.get("college")
        new_teacher = request.form.get("teacher")

        old_course.course_name = new_course_name
        old_course.college = new_college
        old_course.teacher = new_teacher

        db.session.commit()
        return redirect("/course/")
