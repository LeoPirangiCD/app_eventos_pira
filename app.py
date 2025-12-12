from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'database')
os.makedirs(db_path, exist_ok=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Eventos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    idade_minima = db.Column(db.Integer)
    data = db.Column(db.Date)
    hora = db.Column(db.Time)
    cep = db.Column(db.String(20))
    uf = db.Column(db.String(2))
    cidade = db.Column(db.String(100))
    local = db.Column(db.String(200))

def create_tables():
    try:
        with app.app_content():
            db.create_all()

    except Exception:
        db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastrar-evento")
def cadastrar_evento():
    return render_template("cadastrar-evento.html")

if __name__ == "__main__":
    app.run(debug=True)