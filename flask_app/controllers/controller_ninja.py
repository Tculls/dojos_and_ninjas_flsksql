from flask_app.models.model_dojos import Dojo
from flask_app.models.model_ninjas import Ninja
from flask_app import app 
from flask import render_template, request, redirect

@app.route('/ninjas')
def new ():
    return render_template("new_user.html", dojos=Dojo.get_all())

@app.route('/ninjas/create', methods=['POST'])
def ninjaCreate():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/ninjas')