from flask_app.models.model_dojos import Dojo
from flask_app.models.model_ninjas import Ninja
from flask_app import app 
from flask import render_template, request, redirect

@app.route('/dojos/create', methods=['POST'])
def dojoCreate():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')

# @app.route('/dojos')
# def showDojo():
#     return render_template("show_ninjas.html", dojos=Dojo.get_all())

@app.route('/dojos/<int:id>')
def showSingleDojo(id):
    data = {
        "id":id
    }
    return render_template("show_ninjas.html", dojos=Dojo.get_dojo_with_students(data))



# @app.route('/')
# def index():
#     return redirect('/dojos')

# @app.route(f'/dojos/int')
# def dojos():
#     return render_template("index.html")