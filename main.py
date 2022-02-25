from flask import Flask,render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/contacto")
def contacto():
    return render_template("contactos/indexContactos.html")

@app.get("/contacto/<contactoId>/edit")
def editarContacto(contactoId):

    suma = 2022

    return render_template("contactos/editar.html", contactoId = contactoId, suma = suma)  

app.run(debug=True)