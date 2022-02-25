# esto es un comentario de una sola linea

'''
esto es un comentario de multiple comilla sencilla
'''

"""
esto es un comentario de comilla doble
"""

# variables
nombrePersona = 'yilber' #string
edad = 27 # int (entero)
numerodecimal = 10.12 #float (decimales)
esMayorEdad = True #False (booleano)

#debug
print(nombrePersona)

#array (arreglo) listas []
diasSemanas = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
print(diasSemanas[2])

arraymultiple = [1, 'hola, ', [5,6]]
print(arraymultiple[2][1])

# objetos o Diccionarios {}
persona = {
    'nombre': 'yilber',
    'apellidos': 'guevara',
    'edad': 27,
    'lenguajes': ['python', 'javaScript'],
}
print(persona['nombre'])
print(persona['lenguajes'][1])

#lista de diccionarios
personas = [
    {
    'nombre': 'yilber',
    'apellidos': 'guevara',
    'edad': 27,
    'lenguajes': ['python', 'javaScript'],
    },
{
    'nombre': 'luna',
    'apellidos': 'castaño',
    'edad': 16,
    'lenguajes': ['go', 'ruby'],
},
{
    'nombre': 'katerin',
    'apellidos': 'baltazar',
    'edad': 17,
    'lenguajes': ['java', 'flutter'],
}
]
print(personas[1]['lenguajes'][1])

#condiciones

if esMayorEdad == True:
    print("es mayor de edad")
else:
    print("no es mayor de edad")

print ('terminado')