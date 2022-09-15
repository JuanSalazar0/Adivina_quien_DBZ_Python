import mysql.connector

midb=mysql.connector.connect(
    host="localhost",
    user='root',
    password= 'juan1234',
    database='DBZP' 
)

cursor = midb.cursor()
cursor.execute('select * from personaje')
resultado= cursor.fetchall()

cursor.execute('select * from propiedad')
nombres=cursor.fetchall()
#print(resultado)
#id, nombre, sayayin, humano, androide, namek, otroalien, demonio, pelo, vistenaranja, rosa, verde,realeza
#0    1       2          3      4         5      6         7        8      9            10    11    12
#print(resultado[0][1]) #imprime goku 
#consulta de datos 
def Checar_inf(respuesta, dato):
    if respuesta == "y":
        res = 1
    else:
        res = 0
     
    to_remove=[]
    for d in resultado:
        if d[dato] != res:
            to_remove.append(d)
            #print(to_remove)
            #print(resultado)
            #print("si entre")
    for i in to_remove:
        resultado.remove(i)
        #print(to_remove)

    if len(resultado) == 1:
        print("El personaje en el que pensaste es:")
        print( resultado[0][1])
        quit()
       


for z in range(len(nombres)):
    print("Tu personaje tiene la siguiente caracteristica?")
    print(nombres[z][1])
    #print(z)
    respuesta = input("(y/n)" )
    Checar_inf(respuesta, z+2)
    if z == len(nombres): break
