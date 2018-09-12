import random

lista = [random.randint(0, 100) for x in range(random.randint(10, 100))]

print(lista)

lista2 = [x%2 == 0 for x in lista]

print(lista2)     
