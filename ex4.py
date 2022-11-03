lista = eval('['+ input("Informe 5 números reais separados por virgulas: ") +']')
menor = 120000

for i in range(len(lista)):
    if lista[i] < menor:
        menor = lista[i]
        p = i
print(menor,"é o menor número da lista e está na posição", p)