import email
from urllib import response
from xmlrpc.client import ResponseError
from flask import Flask
from flask import render_template, request, redirect, url_for
from flask import Response
from flask_sqlalchemy import SQLAlchemy

import os

# DATOS DE CONEXION A LA BD, CREA LA BD LOCAL EN LA DIRECCION ACTUAL DE TRABAJO EN CASO DE NO ESTAR GENERA DATABASE.DB
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.app_context().push()  #Variable que evita que salga un error

# CLASE PARA LOS MODELOS DE LAS TABLAS
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    email = db.Column(db.String(50))
    mensaje = db.Column(db.String(50))


# se genera la Ruta Index por politca se deben colocar los dos argumentos para que Flask los acepte POST y GET
@app.route("/",methods=["GET", "POST"])
#def index():
#    return "Datos de Airflow"

def form():
    if request.method == 'POST':
        ##usuario = request.form['user_name']
        #email = request.form['user_mail']
        #mensaje = request.form['user_message']
        #next = request.args.get('next', None)
        #documento ='''<html><body><h1> Datos recibidos de Airflow {}</body></html>'''.format(usuario)

        # CAPTURA DE DATOS ENVIADOS POR EL FORMULARIO y SE ENVIAN AL MODELO POST DE LA BD
        new_dato = Posts(usuario = request.form['user_name'], email = request.form['user_mail'], mensaje = request.form['user_message'])
        db.session.add(new_dato)
        db.session.commit()
    #return render_template("signup_form.html")
    #return Response(documento)
    return ("Datos agregados a la BD")

   

if __name__=="__main__":
    db.create_all()
    app.run(debug=True, port=5000)
