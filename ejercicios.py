productos = ['smartphone', 'laptop', 'tablet','smartwatch']
precios = [300, 800, 150, 200]
stock = {
    'smartphone': 20,
    'laptop': 12,
    'tablet': 8,
    'smartwatch': 4
}

max_precio = max(precios)
min_precio = min(precios)

prod_max = productos[precios.index(max_precio)]
prod_min = productos[precios.index(min_precio)]

for prod, precio in zip(productos, precios):
    if precio > 200:
        categoria = 'producto economico'
    elif precio <= 200 and precio <= 500:
        categoria = 'producto estandar'
    else:
        categoria = 'producto premium'
    print(f'{prod}: ${precio} -> {categoria}')
print()
for prod, cantidad in stock.items():
    if cantidad < 10:
        print(f'{prod}: {cantidad} unidades')