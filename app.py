from flask import Flask, render_template, request # Importa la clase Flask
from config import SQLALCHEMY_DATABASE_URI
from database import database
from dotenv import load_dotenv
import os
from flask_migrate import Migrate

app = Flask(__name__) # Intancia de la clase 

@app.route("/primera")
def template_primera():
    return render_template("primera_pagina.html")

@app.route("/condicional")
def condicionales():
    return render_template("condicional.html", equipo="Real")

@app.route("/for-loop")
def for_loop():
    equipos=["Real Madrid",
             "Barcelona", 
             "Atletico de Madrid",
             "Sevilla",
             "Valencia",
             "Independiente de Avellaneda"
             ]
    return render_template(template_name_or_list="for_loop.html", teams=equipos)

usuarios = []

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        info_formulario = request.form.get("contenido")
        usuarios.append(info_formulario)
    return render_template("formulario.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True) # Ejecuta la aplicación en modo debuge