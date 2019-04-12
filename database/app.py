from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

@app . route ( '/' )
def hello (titulo = "Home!!!", lista = ["uno", "dos", "tres"]):	
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route('/insert/default')
def insert_default():
	new_post = Posts(title="Default title")
	db.session.add(new_post)
	db.session.commit()
	return "El default se ha creado"

@app.route('/select/default')
def select_default():
	post = Posts.query.filter_by(id=1).first()
	print(post.title)
	return "Query done."


if __name__ == "__main__":
	db.create_all()
	app.run(debug=True, port=5000, host="127.0.0.1")
