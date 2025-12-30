from flask import Flask , redirect, render_template, url_for

app = Flask(__name__)

@app.route('/new_year')
def new_year():
    return ('Bonne Année 2025 ! Voici une année pleine de promesses.')

if __name__=='__main__':
    app.run(debug=True)