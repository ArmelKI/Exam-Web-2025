
# Web/BD - Examen - Janvier 2025

**Durée :** 1 heure et 50 minutes
**Aucun document autorisés**


## Fraudes et code d'éthique

Afin de garantir l'intégrité et l'équité des examens, il est impératif que chacun respecte les règles éthiques établies. La fraude est non seulement contraire à l'éthique académique, mais elle compromet également la validité des résultats obtenus. Afin de maintenir un environnement d'examen juste et transparent, nous souhaitons vous rappeler quelques directives importantes.

1. **Évitez toute collaboration non autorisée** : Assurez-vous de comprendre clairement les règles en matière de collaboration pendant l'examen. Toute forme de communication non autorisée avec d'autres élèves est strictement interdite.

2. **Surveillance des communications entre ordinateurs** : Soyez conscient que toutes les communications entre les ordinateurs pendant l'examen sont surveillées. L'utilisation de chat, de messagerie instantanée ou d'autres moyens de communication en ligne avec des personnes extérieures à l'examen est une violation des règles.

3. **Évitez le plagiat** : L'utilisation de travaux, de réponses ou de matériel non autorisés, qu'ils soient imprimés ou en ligne, constitue une fraude. Assurez-vous de respecter les règles spécifiques de l'examen concernant l'utilisation de matériel externe.

4. **Utilisation responsable de la technologie** : Les applications tierces, les sites Web non autorisés et tout autre moyen électronique visant à faciliter la fraude sont strictement interdits. L'utilisation d'une technologie qui n'est pas explicitement autorisée par les enseignants peut entraîner des sanctions.

Se conformer à ces directives assure non seulement votre réussite académique, mais garantit également l'équité pour tous les élèves. Tout manquement à ces règles peut entraîner des conséquences sérieuses, y compris des sanctions académiques. Nous comptons sur votre intégrité et votre engagement envers une éducation éthique.


### Documents autorisés

Seuls les documents présents dans le répertoire docs/ sont autorisés (*cheatsheets* et supports de CM). 
Vous pouvez également consulter les documentations suivantes : 
- la [page de la documentation Python](https://docs.python.org/3/library/)
- la [page officielle de la librairie Flask](https://flask.palletsprojects.com/en/stable/)
- le [tutoriel officiel de la librairie Flask](https://flask.palletsprojects.com/en/stable/tutorial/)
- la [page de la documentation SQLite](https://www.sqlite.org/docs.html)


## Mise en place de votre environnement

Il vous est demandé :
- de mettre en place un environnement virtuel pour votre développement ;
- d'y installer les librairies dont vous avez besoin (a minima la librairie `Flask`) ;
- de sauvegarder la liste de vos dépendances dans un fichier `requirements.txt` (pour rappel, cela peut être réalisé en utilisant la commande `pip freeze > requirements.txt`) ;
- de penser **à mettre à jour ce fichier de dépendances** si vous installez plus tard d'autres dépendances.


### Les bases de votre serveur web

Le code principal de votre serveur web devra se trouver dans un fichier Python dénommé `app.py`.

Nous devons être capables d'exécuter votre serveur en utilisant les commandes suivantes :
```bash
# creation d'un environnement virtuel spécifique à l'évaluation
$ python3 -m venv venv
$ source venv/bin/activate

# installation des dépendances
$ pip install -r requirements.txt

# exécution du serveur sur le port 8888 de l'hôte local
$ flask run --host=0.0.0.0 --port=8888
```

**Tout manquement à ces consignes entrainera automatiquement la note de zéro (mauvais nom de fichier, dépendances manquantes, impossibilité d'exécuter votre application).**


## Sujet : Une application de gestion des bonnes résolutions pour 2025 🎉✨

L'objectif de cet examen est de réaliser une application permettant de construire et de consulter une liste de bonnes résolutions pour la nouvelle année.


### Question 1 (1 pts)

En utilisant la bibliothèque Flask, écrire un serveur web qui lors de son exécution retournera la chaîne de caractères (sans les guillemets) `"Bonne Année 2025 ! Voici une année pleine de promesses."` lorsque l'on effectue une requête HTTP `GET` sur la route `/new_year`.


### Question 2 (2 pts)

Considérez la liste de bonnes résolutions suivante représentée sous la forme d'une liste de tuples en Python.
```python
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
```

Chaque bonne résolution (chaque tuple) est composé d'un identifiant unique, d'un intitulé, d'une description, d'un chemin relatif vers une illustration de cette bonne résolution (ou de la valeur `None` si aucune illustration n'est associée), et d'une valeur booléenne indiquant si cette résolution est tenue (réalisée).

Modifier votre application pour qu'une requête HTTP `GET` sur la route `/resolution_by_id/` suivi d'un identifiant d'une résolution retourne une unique chaîne de caractères contenant le nom de la résolution et sa description (les deux étant séparés par le caractère `:`, avec un espace avant et après ce caractère).

À titre d'exemple, une requête sur `/resolution_by_id/3` retournera la chaîne de caractères (sans les guillemets) `"Voyager davantage : Explorer de nouveaux horizons et cultures"`.

Si le nom fourni ne correspond à aucune résolution, la chaîne de caractères (sans les guillemets) `"Aucune bonne résolution ne correspond à cet intitulé"` sera retournée.


### Question 3 (2 pts)

Modifiez votre application pour qu'une requête HTTP `GET` sur la route `/resolution/` suivi de l'identifiant d'une résolution retourne une page HTML affichant les différentes informations concernant cette résolution (les illustrations sont déjà fournies dans le répertoire `static/images/`).

Pour réaliser cela, vous utiliserez un *template* (Jinja) nommé `resolution.html` (à placer dans le répertoire `templates/`).

![Capture d'écran de la page `/resolution/2`](./figures/resolution-annotated.png)
**Figure 1.** Capture d'écran de la page affichée en accédant à la route `/resolution/2`.


### Question 4 (2 pts)

Modifiez votre application pour qu'une requête HTTP `GET` sur la route `/all_resolutions` retourne une page HTML contenant la liste des noms des résolutions. Chaque élément de la liste sera un lien vers la route permettant de consulter les détails de cette résolution (cf. question précédente).

Pour réaliser cela, vous utiliserez un *template* nommé `all_resolutions.html` (à placer dans le répertoire `templates/`).

![Capture d'écran de la page `/all_resolutions`](./figures/all_resolutions-annotated.png)
**Figure 2.** Capture d'écran de la page affichée en accédant à la route `/all_resolutions`.


### Question 5 (2 pts)

Modifiez votre application pour qu'une requête HTTP `GET` sur la route `/add_resolution` retourne une page HTML contenant un formulaire permettant d'ajouter une nouvelle résolution. Le formulaire sera soumis par une requête HTTP `POST` sur la même route que celle qui a permis d'afficher ce formulaire.

Les champs attendus du formulaire sont : `title`, `description`, et `illustration` (uniquement le nom du fichier de l'image que l'on supposera déjà se trouver dans le répertoire `static/images/`).

Pour réaliser cela, vous utiliserez un *template* nommé `add_resolution.html` (à placer dans le répertoire `templates/`).


### Question 6 (2 pts)

Modifiez votre application pour qu'une requête HTTP `POST` sur la route `/add_resolution` traite les données reçues du formulaire précédemment créé et ajoute cette nouvelle résolution à la liste des résolutions. Un identifiant unique devra être généré pour cette nouvelle résolution. On considérera que cette nouvelle résolution n'est pas encore tenue/réalisée (la valeur booléenne associée sera donc initialisée à la valeur `False`).

Une redirection vers la page détaillant la nouvelle résolution ainsi ajoutée sera envoyée en réponse (cette page a été réalisée à la question 3).


### Question 7 (2 pts)

Votre répertoire de travail contient une base de données au format SQLite (`resolutions.db`) et également un fichier SQL contenant le schéma de cette base et les données qui y ont été insérées (`resolutions.sql`).

Modifiez votre application pour qu'une requête HTTP `GET` sur la route `/resolution_from_db/` suivi du nom d'une résolution retourne une page HTML contenant les détails de cette résolution sur le même modèle que celle de la question 3 (vous pouvez réutiliser le même *template*). Dans cette question, les données seront obtenues via une ou des requêtes SQL sur la base de données.


### Question 8 (2 pts)

Modifiez votre application pour qu'une requête HTTP `GET` sur la route `/all_resolutions_from_db` retourne une page HTML (sur le modèle de la question 4) listant toutes les résolutions présentes dans la base de données. Chaque élément de la liste sera un lien vers la route permettant de consulter les détails de cette résolution obtenus à partir de la base de données.

Pour réaliser cela, vous utiliserez un nouveau *template* nommé `all_resolutions_from_db.html` (à placer dans le répertoire `templates/`). Celui-ci est proche de celui réalisé à la question 4 (faites attention aux liens qui doivent maintenant pointer vers la nouvelle route de la question 7).


### Question 9 (3 pts)

Modifiez votre application pour qu'une requête HTTP `GET` sur la route `/add_resolution_to_db` retourne une page HTML permettant d'ajouter une nouvelle résolution à la base de données (sur le modèle de la question 5). Une requête HTTP `POST` sur cette même route traitera la réception des données du formulaire pour mettre à jour la base de données.

Pour réaliser cela, vous utiliserez un nouveau *template* nommé `add_resolution_db.html` (à placer dans le répertoire `templates/`). Celui-ci est proche de celui réalisé à la question 5.


### Question 10 (2 pts)


Modifiez votre application pour qu'une requête HTTP `GET` sur la route `/filtered_resolutions_from_db` retourne une page HTML (sur le modèle de la question 8) listant toutes les résolutions présentes dans la base de données. Chaque élément de la liste sera un lien vers la route permettant de consulter les détails de cette résolution obtenus à partir de la base de données. Cette page permettra de filtrer les résolutions en n'affichant que celles qui sont tenues, ou à tenir, ou toutes les résolutions.

Pour réaliser cela, vous utiliserez un nouveau *template* nommé `filtered_resolutions_db.html` (à placer dans le répertoire `templates/`) et vous devrez probablement ajouter de nouvelles fonctionnalités et/ou des paramètres à votre route existante.

![Capture d'écran de la page `/filtered_resolutions_from_db`](./figures/filtered_resolutions-annotated.png)
**Figure 3.** Capture d'écran de la page affichée en accédant à la route `/filtered_resolutions_from_db`.


### Question 666

Trouver votre chemin à travers le labyrinthe

![Happy New Year](./figures/maze.png)

