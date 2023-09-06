from flask import Flask, render_template
import config
from exts import db
from blueprints.course import bp as course_bp
from blueprints.score import bp as score_bp
from blueprints.student import bp as studednt_bp


# 实例化一个flask对象
app = Flask(__name__)

# 配置这个flask对象：数据库 and ...
app.config.from_object(config)

# 以当前flask对象实例化一个ORM模型 db
db.init_app(app)


# 绑定不同模块对应的蓝图，即视图函数
app.register_blueprint(course_bp)
app.register_blueprint(score_bp)
app.register_blueprint(studednt_bp)


# 主页
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)