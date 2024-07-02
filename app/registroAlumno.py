from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class Registro_Alumno(FlaskForm):
    nombre = StringField('Ingresar Nombre: ',validators=[DataRequired()])
    apellido = StringField('Ingresar Apellido: ',validators=[DataRequired()])
    DNI = PasswordField('Ingresar Clave: ',validators=[DataRequired()])
    email = EmailField('Ingrese Correo Electronico: ',validators=[DataRequired()])
    registrarse = SubmitField('Registrarse')