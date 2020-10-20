def pesquisa_binaria(lista, nome, inicio = 0, fim = None, compara = 0):
    if fim is None:
        fim = len(lista)

    auxiliar = lista[int((inicio + fim)/2)]["first_name"]

    compara += 1

    if(inicio > fim):
        print("Nome não encontrado.")
    elif(nome == auxiliar):
        print("Nome encontrado com ." + compara + " comparações")
        print(lista[int((inicio + fim)/2)])
    else:
        if(nome > auxiliar):
            pesquisa_binaria(lista, nome, int((inicio + fim) / 2), fim, compara)
        else:
            pesquisa_binaria(lista, nome, inicio, int((inicio + fim)/2), compara)