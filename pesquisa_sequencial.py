def pesquisa_sequencial(lista, nome):
    tamanho = len(lista)
    compara = 0
    for i in range(0, tamanho):
        compara += 1
        if(nome == lista[i]["first_name"]):
            print("Nome encontrado com ." + str(compara) + " comparações")
            print(lista[i])
            return
    print("Nome não encontrado com " + str(compara))