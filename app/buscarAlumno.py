from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class buscar_alumno(FlaskForm):
    padron = IntegerField('Ingresar ID del alumno: ', validators=[DataRequired()])
    buscar = SubmitField('Buscar')