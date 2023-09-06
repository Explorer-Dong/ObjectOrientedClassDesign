function confirmDelete(student_id) {
  if (confirm("确定要删除学号为 " + student_id + " 的学生数据吗？")) {
    // 发起 AJAX 请求到后端
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/student-delete/" + student_id, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send("confirmed=true");
  }
}
