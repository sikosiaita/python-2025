#Lista compuesta de datos
lista1 = ['Pia', 18, True]

#Lista compuesta de numeros
n = [1, 2, 3, 4]

#Lista de solo strings
ramos = ['programacion', 'quimica', 'POO']

print(ramos)

#imprimir la posicion del primer elemento de la lista
print(ramos[0])

#funcion count (cuenta la cantidad de concurrencias)
print(ramos.count('programacion'))

#creando e instanciando una tupla
estudiantes = {'luis', 'dayana', 'vale'}
print(type(estudiantes))

#funcion index
print(estudiantes.index('vale'))

#creando sets
colores = {'azul', 'rojo', 'azul', 'verde', 34}
print(colores)

#funcion append
ramos.append('Introduccion a la matematica')
print(ramos)

#modificacr elementos a la lista
ramos[0] = 'quimica'
print(ramos)

#otra forma de insertar un elemento a la lista
ramos.insert(0, 'quimica')
print(ramos)

#eliminando el ultimo elemento de la lista
ramos.pop()
print(ramos)

#ordenando elementos de una lista
ramos.sort()
print(ramos)

#ordenando elementos de una lista segun su cantidad de caracteres
ramos.sort(key=len)
print(ramos)

#ocupando el metodo extend
ramitos = ['calculo', 'automatas']
ramos.extend(ramitos)
print(ramos)