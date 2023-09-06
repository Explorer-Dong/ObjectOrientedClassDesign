function confirm_delete_student(student_number) {
  if (confirm("确定要删除学号为 " + student_number + " 的学生数据吗？")) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/student-delete/" + student_number, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send("confirmed=true");
  }
}

function confirm_delete_score(score_number) {
  if (confirm("确定要删除学号为 " + score_number + " 的成绩数据吗？")) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/score-delete/" + score_number, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send("confirmed=true");
  }
}

function confirm_delete_course(course_number) {
  if (confirm("确定要删除编号为 " + course_number + " 的课程数据吗？")) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/course-delete/" + course_number, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send("confirmed=true");
  }
}
