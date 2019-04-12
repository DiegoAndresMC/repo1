from flask import Flask, render_template
app = Flask (__name__)

@app . route ( '/' )
def hello (titulo = "Home!!!", lista = ["uno", "dos", "tres"]):
	
	
    return render_template("index.html", titulo=titulo, lista=lista)

if __name__ == "__main__":
	app.run(debug=True, port=5000, host="127.0.0.1")