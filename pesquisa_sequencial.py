def pesquisa_sequencial(lista, nome):
    tamanho = len(lista)
    compara = 0
    for i in range(0, tamanho):
        compara += 1
        if(nome == lista[i]["first_name"]):
            print("\t\tNome encontrado após {} comparações.".format(str(compara)) )
            return i
    print("\t\tNome não encontrado após {} comparações.".format(str(compara)) )
    return -1