from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/admin?charset=utf8mb4"

db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/course", methods=["GET", "POST"])
def course():
    return render_template("course.html")


@app.route("/score", methods=["GET", "POST"])
def score():
    return render_template("score.html")


@app.route("/student", methods=["GET", "POST"])
def student():
    return render_template("student.html")


if __name__ == "__main__":
    app.run(debug=True)
