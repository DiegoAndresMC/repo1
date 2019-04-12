from flask import Flask
app = Flask (__name__)

@app . route ( '/' )# Ruta raiz
def index ():
    return 'Hola'

@app.route('/hola')# Otra ruta con nombre hola
def hola():
	return "Holaaa"

@app.route('/user/<string:user>')# ruta con entrada de datos escrito en barra navegador
def user(user):
	app.run()
	return "hola " + user


@app.route('/default/')
@app.route('/default/<string:dft>')
def dft(dft="nada"):
	return "El valor dft es: " + dft

if __name__ == "__main__":
	app.run(debug=True, port=5000, host="127.0.0.1")
