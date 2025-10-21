#Unidad 7 Datos cmplejos - Santisteban - 1prog2
#1) Dado el diccionario precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
print("EJERCICIO 1")
precios_frutas : dict = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(f"Lista de precios actulizada: {precios_frutas}")

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
# actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
print("EJERCICIO 2")
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800
print(f"Lista de precios actulizada: {precios_frutas}")

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
print("EJERCICIO 3")
lista_frutas : list = []
for fruta,precio in precios_frutas.items():
    lista_frutas.append(fruta)
print(f"Lista de frutas {lista_frutas}")
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
print("EJERCICIO 4")
for i in range(5):
    print(i+1,": Datos del contacto:")
    nombre : str = str(input("Ingrese el NOMBRE del contacto: ")) 
    while nombre == "" or nombre ==" ":
        print("Ha ingresado un nombre vacio, intente nuevamente")
        nombre : str = str(input("Ingrese el NOMBRE del contacto: ")) 
    numero = input("Ingrese el NUMERO del contacto: ")
    while not numero.isdigit():
        print("Ha ingresado un caracter letra en lugar de numeros, intente nuevamente")
        numero = input("Ingrese el NUMERO del contacto: ")
    guia_telefonica : dict = {nombre : numero}
contacto_a_buscar :str = str(input("Ingrese un contacto para buscar en la guia telefonica: "))

if contacto_a_buscar in guia_telefonica:
    print(f"El numero de {contacto_a_buscar} es {numero[contacto_a_buscar]}")
else:
        print("El contacto no existe en la guia telefonica")

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra
print("EJERCICIO 5")
frase : str = str(input("Ingrese una frase: "))
frase = frase.lower().split()
palabras_unicas : set = set(frase)
contador : dict = {}
for palabra in frase:
    contador[palabra] = contador.get(palabra,0) + 1
print(f"Palabras unicas de la frase ingersada: {palabras_unicas}")
print(f"Contador de palabras: {contador}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
print("EJERCICIO 6")
alumnos = {}
for i in range(3):
    bandera_nombre : bool = True
    while bandera_nombre == True:
        nombre : str = str(input("Ingrese el nombre del alumno: ")).strip().upper()
        if nombre == "":
            print("El nombre no puede esar vacio, intende nuevamente.")
        elif nombre.upper() in alumnos:
                print("Ese nombre ya fue ingresado, intente con otro.")
        else:
            bandera_nombre = False
    notas = []
    j = 0
    while j < 3:
        bandera_notas : bool = True
        while bandera_notas == True:
            nota : float = float(input(f"Ingrese nota #{j+1} de {nombre} (0 al 10): "))
            if nota == "" or nota == " ":
                print("El valor de la nota no puede quedar vacía.")
            elif nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10.")
            else:
                notas.append(nota)
                bandera_notas = False
        j +=1
    alumnos[nombre] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} tiene un promedio de {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: (interseccion de conjuntos)
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
print("EJERCICIO 7")
parcial_1 : set = ("yoongi","seulgi","mark","wendy","irene","jiwoong","hoshi","jihyo","jeno","chenle")
parcial_2 : set = ("yoongi","jiwoong","irene","taeyong","woozi","vernon","nayeon","jeno","jaemin","seulgi")
print("Estudiantes que aprobaron los parciales 1 y 2 son: ")
for i in parcial_1:
    if i in parcial_2:
        print(i)
print("Estudiantes que aprobaron el parcial 1 son: ")
for i in parcial_1:
    if i not in parcial_2:
        print(i)
print("Estudiantes que aprobaron el parcial 2 son: ")
for i in parcial_2:
    if i not in parcial_1:
        print(i)
print("Estudiantes que aprobaron al menos un parcial son: ")
parciales : set = set(parcial_1 + parcial_2)
print(parciales)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
print("EJERCICIO 8")
bandera : bool = True
productos_varios : dict = {
    "harina": 50,
    "chocolate":23, 
    "azucar": 20,
    "aceite": 30, 
    "mermelada": 10, 
    "licor": 5}
while bandera == True:
    print("------------ CATALOGO DE PRODUCTOS -----------------")
    print("1. Consultar productos")
    print("2. Agregar stock a producto")
    print("3. Agregar producto nuevo")
    print("4. Salir")
    opcion : str = str(input("Ingrese una opcion: "))
    if opcion == "1":
        producto_a_buscar = input("Ingrese el producto por el cual desea consultar: ")
        if producto_a_buscar == "" or producto_a_buscar == " ":
            print("No ha ingresado ningun producto, intente nuevamente")
        else:
            if producto_a_buscar in productos_varios:
                print(f"Producto: {producto_a_buscar} esta disponible en el catalogo")
            else:
                print("No existe el producto por el cual ha consultado.")
    elif opcion == "2":
        producto_a_buscar = input("Ingrese el producto por el cual desea consultar: ")
        if producto_a_buscar == "" or producto_a_buscar == " ":
            print("No ha ingresado ningun producto, intente nuevamente")
        else:
            if producto_a_buscar in productos_varios:
                print(f"Producto: {producto_a_buscar} esta disponible en el catalogo")
                agregar_unidades : int =int(input(f"Cuantas unidades desea agregar al stock de {producto_a_buscar}? " ))
                productos_varios[producto_a_buscar] += agregar_unidades
                print(f"Stock del producto: {producto_a_buscar} : {productos_varios[producto_a_buscar]} ")
            else:
                print("No existe el producto por el cual ha consultado.")
    elif opcion == "3":
        producto_nuevo = input("Ingrese el producto ppara agregar al catalogo: ")
        if producto_nuevo == "" or producto_nuevo == " ":
            print("No ha ingresado ningun producto, intente nuevamente")
        else:
            if producto_nuevo in productos_varios:
                print(f"Producto {producto_nuevo} ya se encuentra en nuestro catalogo, intente nuevamnte!")
            else:
                print("Producto nuevo agregado con exito!")
                agregar_stock : int = int(input(" Ingrese el stock inicial del nuevo producto: "))
                productos_varios[producto_nuevo] += agregar_stock
                print(f"Stock del producto: {producto_nuevo} : {productos_varios[producto_nuevo]} ")

    elif opcion == "4":
        print("Saliendo del menu, gracias!")
        bandera=False
    else:
        print("Ha ingersado una opcion incorrecta, intetnte nuevamente!")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.
print("EJERCICIO 9")
agenda : dict = {
    ("lunes","21:00"):"Aniversario",
    ("martes","19:45"):"Clase de apoyo",
    ("miercoles","16:00"):"Parcial",
    ("jueves","09:15"):"Yoga",
    ("viernes","15:30"):"Juntada"
}
print("------------Consultar eventos---------")
consulta_dia = input("Que dia desea consultar si hay un evento?: ").lower()
consulta_hora = input("En que horario quiere consultar si hay un evento? (formato hora hh:mm pm): ")
evento = (consulta_dia,consulta_hora)
if evento in agenda:
    print(f"La activdad del {consulta_dia} a las {consulta_hora} es {agenda[evento]}")
else:
    print(f"No hay nada programado para el el {consulta_dia} a las {consulta_hora}")



#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
print("EJERCICIO 10")
paises = {"Argentina": "Buenos Aires","Chile": "Santiago","Corea del Sur": "Seul","Inglatera":"Londres","Perú": "Lima"}
paises_invertidos : dict = {}
for pais, capital in paises.items():
    paises_invertidos[capital]=pais
print("Diccionario original:", paises)
print("Diccionario invertido:", paises_invertidos)