from wtforms import Form
from wtforms import StringField,TelField,IntegerField
from flask_wtf import FlaskForm
from wtforms import EmailField
from wtforms import validators


class UserForm2(Form):
    id=IntegerField('id',[validators.number_range(min=4,max=20, message='Ingresa nombre valido')])
    nombre= StringField('nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa nombre valido')
    ])
    direccion= StringField('direccion',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa direccion valido')
    ])
    telefono= StringField('telefono',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa telefono valido')
    ])
    email= EmailField('email',[
        validators.Email(message='Ingresa un email valido')
    ])
    sueldo= StringField('sueldo',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa sueldo valido')
    ])