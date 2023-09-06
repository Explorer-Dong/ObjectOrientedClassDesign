from models import Course

from .base_module import BaseModule

class CourseModule(BaseModule):
    def __init__(self):
        super().__init__("course", __name__, url_prefix="/")

    def course(self):
        return self.search_items(Course, Course.name, "form_course", "course.html")

    def course_add(self):
        return self.add_item(Course, "course-add.html")

    def course_delete(self, number):
        return self.delete_item(Course, number)

    def course_correct(self, number):
        return self.correct_item(Course, "course-correct.html", number)

bp = CourseModule()

bp.add_url_rule("/course/", view_func=bp.course, methods=["GET", "POST"])
bp.add_url_rule("/course-add/", view_func=bp.course_add, methods=["GET", "POST"])
bp.add_url_rule("/course-delete/<string:number>", view_func=bp.course_delete, methods=["GET", "POST"])
bp.add_url_rule("/course-correct/<string:number>", view_func=bp.course_correct, methods=["GET", "POST"])
