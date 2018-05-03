from flask import Flask, request, render_template
from Pokedex import find_your_pokemon

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return render_template('form.html',name=find_your_pokemon(text))