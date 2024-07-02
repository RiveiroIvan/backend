from flask import Flask, render_template, request, redirect, url_for, flash, g, abort, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from buscarAlumno import buscar_alumno
from registroAlumno import Registro_Alumno

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy()
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = '12ike90123ur0j209'


from dates import Dates
# from config import Config
# from static import models
# from init import SQLAlchemy

@app.route("/")
@app.route("/escuela")
def escuela():
    return render_template("escuela.html")

@app.route('/registro')
def registro():
    form = Registro_Alumno()
    if form.validate_on_submit():
        nombre_viejo = session.get('nombre')
        if nombre_viejo is not None and nombre_viejo != form.nombre.data:
            session['nombre'] = form.nombre.data
            form.nombre.data = ''
            return redirect(url_for('registro'))
    return render_template('registro.html', form=form, nombre=session.get('nombre'))

@app.route("/buscar", methods=['GET', 'POST'])
def busqueda():
    busqueda = buscar_alumno()
    if request.method == 'POST':
        if busqueda.validate_on_submit():
            padron = busqueda.padron.data
            return redirect(url_for("buscarAlumno", padron=padron))
        else:
            flash("Se debe ingresar un padrón")
    return render_template("buscarAlumno.html", form=busqueda)

@app.route('/buscar/<int:padron>', methods=['GET', 'POST'])
def identificar(padron):
    identificar_estudiante = next((estudiante for estudiante in g.estudiantes if estudiante.patron == padron), None)
    if identificar_estudiante is None:
        return abort(404)
    return render_template('studente.html', estudiante=identificar_estudiante)

@app.route('/studiantes')
def estudiantes():
    return render_template('estuantes.html', estudiantes=g.estudiantes)

@app.route("/sesion", methods=['GET', 'POST'])
def sesion():
    if request.method == 'POST':
        I_email = request.form['I_correo']
        I_clave = request.form['I_clave']
        
        user = Dates.query.filter_by(email=I_email, clave=I_clave).first()
        
        if user:
            flash('Inicio de sesión exitoso')
            return redirect(url_for('escuela'))
        else:
            flash('Correo o contraseña incorrectos')
    return render_template('I.sesion.html')

if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/registro" , methods=['GET', 'POST'])
# def registro():
    # if request.method == 'POST':
    # R_usuario = request.form['R_usuario']
    # R_email = request.form['R_email']
    # R_clave = request.form['R_clave']
    
    # if R_usuario and R_email and R_clave:
    # new_user = User(usuario=R_usuario , correo=R_email, clave=R_clave)
    # try:
    # db.session.add(new_user)
    # db.session.commit()
    # return redirect(url_for('login'))
    # except Exception as e:
    # db.session.rollback()
    # flash ('error al ejecutar la consulta {e}')
    # else
        # flash ('Llena todos los campos')
# return render_template('I.sesion.html')
    
# app.route("/sesion" , methods=['GET', 'POST'])
# def sesion():
    # if request.method == 'POST':
    # I_email = request.form['I_correo']
    # I_clave = request.form['I_clave']
    
    # user = User.query.filter_by(email=I_email, clave=I_clave).first()
    
    # if user:
            # flash('Inicio de sesión exitoso')
            # return redirect(url_for('escuela'))
        # else:
            # flash('Correo o contraseña incorrectos')
    # return render_template('login.html')
    
# if __name__ == "__main__":
    # with app.app_context():
    # db.create_all()
    # app.run(debug=True)