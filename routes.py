from flask import render_template, redirect, url_for
from app import app 

resolutions = [
    (
        1,
        "Faire plus d'exercice",
        "Se remettre en forme avec des activités régulières",
        "images/exercise.jpg",
        False,
    ),
    (
        2,
        "Apprendre une nouvelle compétence",
        "Élargir ses horizons avec une compétence utile",
        "images/skill.jpg",
        False,
    ),
    (
        3,
        "Voyager davantage",
        "Explorer de nouveaux horizons et cultures",
        "images/travel.jpg",
        False,
    ),
    (
        42,
        "Économiser plus",
        "Planifier un avenir financier sûr",
        "images/savings.jpg",
        False,
    ),
    (
        5,
        "Passer plus de temps avec ses proches",
        "Renforcer les liens familiaux et amicaux",
        "images/family.jpg",
        True,
    ),
]

@app.route('/new_year')
def new_year():
    return 'Bonne Année 2025 ! Voici une année pleine de promesses.'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resolution_by_id/<int:res_id>')
def resolution_by_id(res_id):
    for res in resolutions:
        if res[0]==res_id:
            return f"{res[1]} : {res[2]}"
    return "Aucune bonne résolution ne correspond à cet intitulé"