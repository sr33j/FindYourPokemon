from flask import Flask, request, render_template
from Pokedex import find_your_pokemon

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html',name="")

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    text = request.form['text']
    spirit_pokemon = find_your_pokemon(text)
    image_path = "minipokemon/"+spirit_pokemon+".jpg"
    return render_template('form.html',name=spirit_pokemon, link=image_path)