#creando sets
colores = {'azul', 'rojo', 'azul', 'verde'}
colorcitos = {'azul', 'naranjo'}

#imprimiendo el set colores
print(colores)

#agregando un nuevo elemento al set
colores.add('blanco')
print(colores)

#eliminando un elemento del set
colores.discard('blanco')
print(colores)

#aplicando el metodo difference
diferencia = colores.difference(colorcitos)
print(diferencia)