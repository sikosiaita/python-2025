entero = (int(input("Ingrese el primer numero (entero): ")))
flotante = (float(input("Ingrese el segundo numero (decimal): ")))
complejo = (complex(input("Ingrese el tercer numero (complejo (su numero debe terminar con una j)): ")))

potencia_compleja = (complejo**entero)
suma_mixta = (complejo+flotante)
producto_mixto = (complejo*entero)
vapoco = abs(complejo**entero)

print(f"La potencia compleja es: {potencia_compleja}")
print(f"La suma mixta es: {suma_mixta}")
print(f"El producto mixto es: {producto_mixto}")
print(f"El módulo del número complejo es: {vapoco:.3f}")