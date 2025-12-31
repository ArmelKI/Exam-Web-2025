from flask import render_template, redirect, url_for, request
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
    
@app.route('/resolution/<int:res_id>')
def resolution(res_id):
    for res in resolutions:
        if res[0]==res_id:
            return render_template('resolution.html', resolution=res)
    
    return "Résolution non trouvée" 

@app.route('/all_resolutions')
def all_resolutions():
    return render_template('all_resolutions.html', resolutions = resolutions)

@app.route('/add_resolution', methods=['GET', 'POST'])
def add_resolution():
    if request.method=='POST':
        title = request.form.get('title')
        description = request.form.get('description')
        image_name = request.form.get ('illustration')

        existing_ids=[res[0] for res in resolutions]
        new_id= max(existing_ids)+1 if existing_ids else 1
        image_path = f"images/{image_name}" if image_name else None
        new_resolution = (new_id, title, description, image_path, False )

        resolutions.append(new_resolution)
        return redirect(url_for('resolution', res_id = new_id))
    
    return render_template('add_resolution.html')