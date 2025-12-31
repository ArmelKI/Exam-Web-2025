from flask import render_template, redirect, url_for
from app import app 

@app.route('/new_year')
def new_year():
    return 'Bonne Année 2025 ! Voici une année pleine de promesses.'
