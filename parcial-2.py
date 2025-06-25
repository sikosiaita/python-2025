#LETRA A
vet = {
    101 : {
        'NOMBRE' : 'LUNA',
        'PESO' : 1.2,
        'EDAD' : 3,
        'TAMAÑO' : 30
    },
    102 : {
        'NOMBRE' : 'MICHI',
        'PESO' : 0.8,
        'EDAD' : 2,
        'TAMAÑO' : 25
    },
    103 : {
        'NOMBRE' : 'PEPITO',
        'PESO' : 2.5,
        'EDAD' : 5,
        'TAMAÑO' : 35
    }
}
print(vet)

#LETRA B
for clasificacion, pesos in vet.items():
    clasi = pesos['PESO']
    if clasi < 1:
        clasificacion = 'bajo peso'
    elif 1 <= clasi <= 4:
        clasificacion = 'normal'
else:
    clasificacion = 'sobre peso'
pesos['CLASIFICACION-PESO'] = clasificacion

print(vet)

#LETRA C
for categoria, edad in vet.items():
    etaria = edad['EDAD']
    if etaria < 4:
        categoria = 'cachorro'
    elif 1 <= etaria <= 4:
        categoria = 'joven',
else:
    categoria = 'adulto'
edad['CATEGORIA-ETARIA'] = categoria
print(vet)

#LETRA D
listatupla = [tuple(101), tuple(1.2), tuple(102), tuple(0.8), tuple(103), tuple(2.5)]
print(len(listatupla))

#LETRA F
input('INGRESE UN NUMERO DE GATITO EXISTENTE (101, 102, 103) CON SU TAMAÑO')

#LETRA G
lista_peso= [1.2, 0.8, 2.5]
prom = (1.2 + 0.8 + 2.5)/3
print(prom)
print(max(lista_peso))
print(min(lista_peso))
print(lista_peso.index(0.8))
