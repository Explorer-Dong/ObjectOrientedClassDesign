from models import Student
from .base_module import BaseModule


class StudentModule(BaseModule):
    def __init__(self):
        super().__init__("student", __name__, url_prefix="/")


    def student(self):
        return self.search_items(Student, Student.name, "form_student", "student.html")


    def student_add(self):
        return self.add_item(Student, "student-add.html")


    def student_delete(self, number):
        return self.delete_item(Student, number)


    def student_correct(self, number):
        return self.correct_item(Student, "student-correct.html", number)

bp = StudentModule()

bp.add_url_rule("/student/", view_func=bp.student, methods=["GET", "POST"])
bp.add_url_rule("/student-add/", view_func=bp.student_add, methods=["GET", "POST"])
bp.add_url_rule("/student-delete/<string:number>", view_func=bp.student_delete, methods=["GET", "POST"])
bp.add_url_rule("/student-correct/<string:number>", view_func=bp.student_correct, methods=["GET", "POST"])
