from flask_app.models.model_dojos import Dojo
from flask_app.models.model_ninjas import Ninja
from flask_app import app 
from flask import render_template, request, redirect

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("index.html", dojos=Dojo.get_all())





# @app.route