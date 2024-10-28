#importar librerias
from flask import Flask, render_template

#variable de control
N1=Flask(__name__)
#rutas

@N1.route('/')
def inicio():
    return render_template("inicio.html")

@N1.route('/sobre')
def sobre():
    return render_template("sobrenosotros.html")
    
@N1.route('/servi')
def servicios():
    return render_template("servicios.html")

@N1.route('/portafolio')
def portafolio():
    return render_template("portafolio.html")

@N1.route('/ubicacion')
def ubi():
    return render_template("ubicacion.html")

if __name__=='__main__':
    N1.run(debug=True)
