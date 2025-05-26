"""GUIA TIPO DE DATOS PYTHON"""

#INICIALIZANDO VARIABLES NUMERICAS
edad=18
estatura=1.65
peso=50
complejo = 2 + 9j
complejo2 = complex(1, 4)

print(complejo)
print(complejo2)

#operacion aritmetica
imc = peso / (estatura ** 2) 
print(f"Su IMC es: {imc}")

print ("Su IMC es: {:.2f}".format(imc))

#transformando numero entero a decimal con FLOAT
print (float(edad))

print(round(imc, 2))

#Datos en cadena de texto

carrera='ingenieria civil en informatica'
asignatura='programacion'
descripcion='esto es una asignatura de primer año'

#impresion de caracteres en una cadena de texto
print(carrera [0])
print(carrera[-1])

print("Hola"*4)
#no se puede dividir una palabra por 4

#Aplicando split intervalo de cadena
print(asignatura[0:5])

#Aplicando metodo split (genera un arreglo de cadena)
print(descripcion.split)

#arreglo numerico
v = [1, 2, 3, 3, 5] #inicializando un arreglo numerico
print(v[0])

len(carrera)
print (f"La palabra {carrera} tiene: ", len(carrera))

#valores booleanos
interruptor = True
ampolleta = False

#funcion type permite saber el tipo de dato que se utiliza
print(type(interruptor))

#comparativa de valores logicos
"""print(1<10)
print(100<=20)
print(100==100)"""

print(bool(""))
print(bool(1))
print(bool(0))