from flask import Flask, render_template
import config
from exts import db, mail
from blueprints.course import bp as course_bp
from blueprints.score import bp as score_bp
from blueprints.student import bp as student_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate

# 实例化一个flask对象
app = Flask(__name__)

# 配置这个flask对象：数据库
app.config.from_object(config)

# 将当前flask对象绑定一个ORM模型 db和一个邮件对象 mail
db.init_app(app)
mail.init_app(app)

# 将ORM模型与数据库进行同步
migrate = Migrate(app, db)

# 绑定不同模块对应的蓝图，即视图函数
app.register_blueprint(course_bp)
app.register_blueprint(score_bp)
app.register_blueprint(student_bp)
app.register_blueprint(auth_bp)


# 主页
@app.route("/")
def index():
	return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True)
