"""GUIA INICIAL DE PYTHON
DE VARIABLES - ULAGOS 2025"""

nombre = "Pia" 
apellido = "Rojas"

print("Hola mi nombre es ", nombre, "y mi apellido es ", apellido)


#imprimiendo con operador de concatenación
print("Hola mi nombre es " + nombre, "y mi apellido es " + apellido)

#imprimiendo con cadenas f-string

print (f"Hola mi nombre es {nombre} y mi apellido es {apellido}")

ciudad, region, pais = "Castro", "Los Lagos", "Chile"

print (f"Hola soy de {ciudad}, {region}, {pais}")

#usando input
print (nombre)
nombre = input ("Ingrese su nombre")
print (f"Hola, mi nombre es: {nombre}")

print (nombre)