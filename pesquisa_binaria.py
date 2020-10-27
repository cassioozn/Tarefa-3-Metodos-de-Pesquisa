def pesquisa_binaria(lista, nome, inicio = 0, fim = None, compara = 0):
    if fim is None:
        fim = len(lista) - 1

    meio = (inicio + fim)/2
    meio = int(meio)

    auxiliar = lista[meio]["first_name"]

    compara += 1

    if inicio > fim:
        print("Nome não encontrado.")
    elif(nome == auxiliar):
        print("Nome encontrado com ." + str(compara) + " comparações.\n")
        print(lista[meio])
    else:
        if nome > auxiliar:
            pesquisa_binaria(lista, nome, meio - 1, fim, compara)
        else:
            pesquisa_binaria(lista, nome, inicio, meio + 1, compara)