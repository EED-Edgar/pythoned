lista = eval('['+ input("Informe 10 números inteiros separados por virgulas: ") +']')
maior = -10000
pos = 0

for i in range(10):
    if lista[i]>maior:
        maior = lista[i]
        pos = i

print(maior,"é o maior número da lista e está na posição", pos)