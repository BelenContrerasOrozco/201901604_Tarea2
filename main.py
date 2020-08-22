#JSON
import json

def readJson():
    file = open('201901604_Tarea2\Registro1.json')
    data = json.load(file)
    file.close()
    print("     ")
    print("--------------------------------ARCHIVOS JSON--------------------------------")
    return data
    
dict = readJson()
for element in dict:
    print(element)


#CSV
import csv

with open('201901604_Tarea2\Registro3.csv') as f:
    reader = csv.reader(f)
    print("     ")
    print("--------------------------------ARCHIVOS CSV---------------------------------")
    for row in reader:
        print("Nombre: {0}, Apellido: {1}, Edad: {2}, Departamento: {3}".format(row[0], row[1], row[2], row[3]))


#XML
from xml.dom import minidom
print()
print("--------------------------------ARCHIVOS XML---------------------------------")
archivo = minidom.parse("201901604_Tarea2/Registro2.xml")
todoscursos = archivo.getElementsByTagName("curso")

for chid in todoscursos:
    nombre = chid.getElementsByTagName("nombre")[0]
    creditos =chid.getElementsByTagName("creditos")[0]
    catedratico = chid.getElementsByTagName("catedratico")[0]
    seccion = chid.getElementsByTagName("seccion")[0]
    
    print("nombre: %s" % nombre.firstChild.data)
    print("creditos: %s" % creditos.firstChild.data)
    print("catedratico: %s" % catedratico.firstChild.data)
    print("seccion: %s" % seccion.firstChild.data)
    print("     ")