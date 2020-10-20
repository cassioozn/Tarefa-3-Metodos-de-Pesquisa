def pesquisa_sequencial(lista, nome):
    tamanho = len(lista)
    compara = 0
    for i in range(0, tamanho):
        auxiliar = lista[i]["first_name"]
        compara += 1
        if(nome == auxiliar):
            print("Nome encontrado com ." + str(compara) + " comparações")
            print(lista[i])
            break