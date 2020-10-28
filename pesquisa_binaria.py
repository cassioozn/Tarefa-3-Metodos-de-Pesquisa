def pesquisa_binaria(lista, nome, inicio = 0, fim = None, compara = 0):
    if fim is None:
        fim = len(lista) - 1

    meio = int((inicio + fim)/2)

    auxiliar = lista[meio]["first_name"]

    compara += 1

    if inicio > fim:
        print("\t\tEntrada não encontrada após {} comparações.".format(str(compara)) )
        return -1
    elif(nome == auxiliar):
        print("\t\tEntrada encontrada após {} comparações:".format(str(compara)) )
        return meio
    else:
        if nome > auxiliar:
            return pesquisa_binaria(lista, nome, meio + 1, fim, compara)
        else:
            return pesquisa_binaria(lista, nome, inicio, meio - 1, compara)