from models import Course
from flask import request

from .base_module import BaseModule

bp = BaseModule("course", __name__, url_prefix="/")


@bp.route("/course/", methods=["GET", "POST"])
def course():
	# 模型类，搜索字段，表单名，模板名
	return bp.search_items(Course, Course.name, "form_course", "course.html")


@bp.route("/course-add/", methods=["GET", "POST"])
def course_add():
	# 模型类，增加界面模板名
	return bp.add_item(Course, "course-add.html")


@bp.route("/course-delete/<string:number>", methods=["GET", "POST"])
def course_delete(number):
	# 模型类，目标
	return bp.delete_item(Course, number)


@bp.route("/course-correct/<string:number>", methods=["GET", "POST"])
def course_correct(number):
	# 模型类，修改界面模板名，目标
	return bp.correct_item(Course, "course-correct.html", number)