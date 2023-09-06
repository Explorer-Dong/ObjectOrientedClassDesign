from models import Score
from .base_module import BaseModule


class ScoreModule(BaseModule):
    def __init__(self):
        super().__init__("score", __name__, url_prefix="/")


    def score(self):
        return self.search_items(Score, Score.name, "form_score", "score.html")


    def score_add(self):
        return self.add_item(Score, "score-add.html")


    def score_delete(self, number):
        return self.delete_item(Score, number)


    def score_correct(self, number):
        return self.correct_item(Score, "score-correct.html", number)

bp = ScoreModule()

bp.add_url_rule("/score/", view_func=bp.score, methods=["GET", "POST"])
bp.add_url_rule("/score-add/", view_func=bp.score_add, methods=["GET", "POST"])
bp.add_url_rule("/score-delete/<string:number>", view_func=bp.score_delete, methods=["GET", "POST"])
bp.add_url_rule("/score-correct/<string:number>", view_func=bp.score_correct, methods=["GET", "POST"])
