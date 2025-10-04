from flask import Flask, render_template, request
from config import DATABASE_URI
from database import database
from dotenv import load_dotenv
from flask_migrate import Migrate
import os

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.getenv("SECRET_KEY")

database.init_app(app)
migrate = Migrate(app, database)

@app.route("/")
def inicio():
    return render_template("base.html")





if __name__ == "__main__":
    app.run(debug=True)

















""" 
usuarios = ["Tomas", "Juan", "Ana", "Maria"]

@app.route("/")
def lista_usuarios():
    return render_template("index.html", users=usuarios)

    @app.route("/primera")
    def template_primera():
        return render_template("primera_pagina.html")

    @app.route("/condicional")
    def condicionales():
        return render_template("condicional.html", equipo="Real")

    @app.route("/for-loop")
    def for_loop():
        equipos = [
            "Real Madrid",
            "Barcelona",
            "Atletico de Madrid",
            "Sevilla",
            "Valencia",
            "Independiente de Avellaneda"
        ]
        return render_template("for_loop.html", teams=equipos)

    usuarios = []

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            info_formulario = request.form.get("contenido")
            parametros = {"nombre": info_formulario}
            usuarios.append(parametros)
            app.database.usuarios.insert().values(parametros)
            print(usuarios)
        return render_template("formulario.html", usuarios=usuarios)
"""
