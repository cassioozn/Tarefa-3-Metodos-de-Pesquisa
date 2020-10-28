def pesquisa_sequencial(lista, nome):
    tamanho = len(lista)
    compara = 0
    for i in range(0, tamanho):
        compara += 1
        if(nome == lista[i]["first_name"]):
            print("\t\tEntrada encontrada após {} comparações:".format(str(compara)) )
            return i
    print("\t\tEntrada não encontrada após {} comparações.".format(str(compara)) )
    return -1