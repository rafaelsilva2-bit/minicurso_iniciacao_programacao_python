lista = []
condicao = True
while condicao:
    print("lista de compras")
    print()
    print("1) Add item")
    print("2) Remover item")
    print("3) mostrar itens")
    print("0)")
    resposta = int(input("Digite uma opção:"))
    if resposta == 1:
        print("O que deseja adicionar?")
        item = input()
        lista.append(item)
    if resposta == 2:
        print("O que deseja remover?")
        item = input()
        lista.pop(item)
    if resposta == 3:
        print()
        for elemento in lista:
            print(elemento)
        print()
    if resposta == 0:
        condicao = False

