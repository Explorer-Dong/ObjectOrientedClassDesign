from flask import Blueprint, request, render_template, redirect
from exts import db
from models import Score


bp = Blueprint("score", __name__, url_prefix="/")


# 分数表：主页 + 搜索
@bp.route("/score/", methods=["GET", "POST"])
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
@bp.route("/score-add/", methods=["GET", "POST"])
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
@bp.route("/score-delete/<string:score_number>", methods=["GET", "POST"])
def score_delete(score_number):
    if request.method == "POST":
        if request.form.get("confirmed") == "true":
            score = Score.query.filter(Score.number == score_number).first()
            db.session.delete(score)
            db.session.commit()
    return redirect("/score")


# 分数表：修改，传入的参数是学号
@bp.route("/score-correct/<string:score_number>", methods=["GET", "POST"])
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
