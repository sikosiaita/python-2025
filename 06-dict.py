#creando diccionario (se agregan diferentes tipos de datos estructurados)
paciente = {
    'nombre': 'carlos',
    'apellido': 'santana',
    'edad': 50,
    'ciudad': 'Quellon',
    'consultas': [14, 20, 40],
    'diagnostico': {'resfriado'}
}
print(paciente)

#otra forma de declarar diccionario
medico = dict(
    nombre = 'samir',
    apellido = 30,
    especialidad = 'neurologo'
)
print(medico)

#consultando un elemento a traves de la clave del diccionario
print(medico['nombre'])

#eliminando una clave del diccionario (metodo "DEL" (DELETE))
del(paciente['nombre'])
print(paciente)