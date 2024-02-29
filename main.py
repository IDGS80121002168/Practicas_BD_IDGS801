from flask import Flask, render_template, request, flash
from flask_wtf.csrf import CSRFProtect
from wtforms import Form, StringField, IntegerField, EmailField, validators
from config import DevelopmentConfig
from flask import g

import forms
from models import db, Empleados

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/index", methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST':
        try:
            empl = Empleados(
                nombre=create_form.nombre.data,
                direccion=create_form.direccion.data,
                telefono=create_form.telefono.data,
                email=create_form.email.data,
                sueldo=create_form.sueldo.data,

            )
            db.session.add(empl)
            db.session.commit()
        except Exception as e:
            print(f"Error en la base de datos: {e}")
            db.session.rollback()
    return render_template('index.html', form=create_form)


@app.route("/ABC_Completo", methods=["GET", "POST"])
def ABCompleto():
    emple = forms.UserForm2(request.form)
    empleado = Empleados.query.all()
    print(empleado)  
    return render_template("ABC_Completo.html", empleado=empleado)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run()
