from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/admin?charset=utf8mb4"

db = SQLAlchemy(app)


with app.app_context():
    with db.engine.connect() as con:
        rs = con.execute(text("select 1"))
        print(rs.fetchone())


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
