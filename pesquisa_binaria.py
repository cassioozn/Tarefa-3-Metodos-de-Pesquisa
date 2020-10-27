def pesquisa_binaria(lista, nome, inicio = 0, fim = None, compara = 0):
    if fim is None:
        fim = len(lista) - 1

    meio = int((inicio + fim)/2)

    auxiliar = lista[meio]["first_name"]

    compara += 1

    if inicio > fim:
        print("Nome não encontrado com." + str(compara) + "comparações.\n")
    elif(nome == auxiliar):
        print("Nome encontrado com ." + str(compara) + " comparações.\n")
        print(lista[meio])
    else:
        if nome > auxiliar:
            pesquisa_binaria(lista, nome, meio + 1, fim, compara)
        else:
            pesquisa_binaria(lista, nome, inicio, meio - 1, compara)