from models import Student
from flask import request

from .base_module import BaseModule

bp = BaseModule("student", __name__, url_prefix="/")


@bp.route("/student/", methods=["GET", "POST"])
def student():
    # 模型类，搜索字段，表单名，模板名
    return bp.search_items(Student, Student.name, "form_student", "student.html")


@bp.route("/student-add/", methods=["GET", "POST"])
def student_add():
    # 模型类，增加界面模板名
    return bp.add_item(Student, "student-add.html")


@bp.route("/student-delete/<string:number>", methods=["GET", "POST"])
def student_delete(number):
    # 模型类，目标
    return bp.delete_item(Student, number)


@bp.route("/student-correct/<string:number>", methods=["GET", "POST"])
def student_correct(number):
    # 模型类，修改界面模板名，目标
    return bp.correct_item(Student, "student-correct.html", number)