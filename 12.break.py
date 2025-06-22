#break
while True:
    parametro = input(">")
    if parametro == "Salir":
        break
    else:
        print(parametro)

n = 0

#continue
while n <= 50:
    n += 1
    if n == 40:
        continue
    print(n)

#for
newlista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in newlista:
    print(i)

for i in range(1,11):
    print(i)