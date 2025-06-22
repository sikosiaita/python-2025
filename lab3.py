registros = {
    5700000 : {
        'CIUDAD' : 'CASTRO',
        'TEMPERATURA' : 11.8,
        'PRECIPITACION TOTAL' : 2000
    },
    5770000 : {
        'CIUDAD' : 'CHONCHI',
        'TEMPERATURA' : 8.3,
        'PRECIPITACION' : 2800
    },
    5790000 : {
        'CIUDAD' : 'QUELLON',
        'TEMPERATURA' : 10.2,
        'PRECIPITACION' : 2950
    }
}
print(registros)

for codigo, datos in registros.items():
    
    temp = datos['TEMPERATURA']
    if temp < 10:
        clima = 'FRIO'
    elif 10 <= 15:
        clima = 'TEMPLADO',
else:
    clima = 'CALIDO'
datos['CLIMA'] = clima
print(registros)

registros[5700000].update({'MESES MAS LLUVIOSOS' : []})
print(registros)



registros[5770000]['CIUDAD'] = 'CIUDAD DE LOS TRES PISOS'
print(registros)

lluvias= [2000, 2800, 2950]
print('La suma de las tres precipitaciones es: ', sum(lluvias))
print('La precipitacion minima es: ', min(lluvias))
print('La precipitacion maxima es: ', max(lluvias))
print('El indice de la precipitacion mas alta es: ', lluvias.index(2950))
print(registros)

lista_tuplas = list(registros.items())
from pprint import pprint
pprint(lista_tuplas)    