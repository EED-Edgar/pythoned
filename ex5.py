lista = eval('['+ input("Informe 8 números inteiros separados por virgulas: ") +']')
media = 0
for i in range(len(lista)):
    media = media + lista[i]
    if i == len(lista) - 1:
        media = media/int(len(lista))
for i in range(len(lista)):
    if lista[i] > media:
        print(lista[i])