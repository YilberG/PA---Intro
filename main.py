from flask import Flask,render_template
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='baseproductos',
    port=3306
)
db.autocommit = True

app = Flask(__name__)

@app.get("/")
def index():
    cursor = db.cursor(dictionary=True)


    cursor.execute('select * from productos')

    productos = cursor.fetchall()
    #productos = cursor.fetchone() "este es solo para traer un solo producto"
    #print(productos[1]['Nombre']) "solo para ver la informacion"

    cursor.close()
    return render_template("index.html",productos=productos)

@app.get("/contacto")
def contacto():
    return render_template("contactos/indexContactos.html")

@app.get("/contacto/<contactoId>/edit")
def editarContacto(contactoId):

    suma = 2022

    return render_template("contactos/editar.html", contactoId = contactoId, suma = suma)  

app.run(debug=True)