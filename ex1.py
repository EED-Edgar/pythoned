lista = eval('['+ input("Coloque uma lista de idades separadas por virgulas: ") +']')
for i in range(len(lista)):
    if(i%2 == 0):
        print(lista[i])