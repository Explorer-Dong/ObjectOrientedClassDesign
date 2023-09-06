from models import Score
from flask import request

from .base_module import BaseModule

bp = BaseModule("score", __name__, url_prefix="/")


@bp.route("/score/", methods=["GET", "POST"])
def score():
    # 模型类，搜索字段，表单名，模板名
    return bp.search_items(Score, Score.name, "form_score", "score.html")


@bp.route("/score-add/", methods=["GET", "POST"])
def score_add():
    # 模型类，增加界面模板名
    return bp.add_item(Score, "score-add.html")


@bp.route("/score-delete/<string:number>", methods=["GET", "POST"])
def score_delete(number):
    # 模型类，目标
    return bp.delete_item(Score, number)


@bp.route("/score-correct/<string:number>", methods=["GET", "POST"])
def score_correct(number):
    # 模型类，修改界面模板名，目标
    return bp.correct_item(Score, "score-correct.html", number)