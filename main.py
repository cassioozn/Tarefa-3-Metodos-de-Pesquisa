# coding: utf-8

from csv import DictReader
import json

import pesquisa_binaria
import pesquisa_sequencial
import sys

def main():

    #================================================================================
    # Constantes e pré-carregamento de arquivos
    #================================================================================

    comprimento_linhas = 80

    # Lista com os caminhos dos arquivos nos quais será efetuada a busca.
    lista_caminhos = [
    "datasets_prontos/1000/crescente.csv",
    "datasets_prontos/2000/crescente.csv",
    "datasets_prontos/3000/crescente.csv",
    "datasets_prontos/5000/crescente.csv"
    ]

    lista_nomes = [] # Lista que será preenchida com os nomes

    # Preenche a lista com os nomes do arquivo.
    with open("nomes_para_busca.txt", "r") as arquivo_nomes:
        for nome in arquivo_nomes.readlines():
            lista_nomes.append(nome.strip())

    #================================================================================
    # Parte da pesquisa sequencial
    #================================================================================
    print("="*comprimento_linhas)
    print("\tPESQUISA SEQUENCIAL")
    print("="*comprimento_linhas)

    for caminho in lista_caminhos:

        print("\tRealizando pesquisas no arquivo \"{}\"...".format(caminho))
        print("-"*comprimento_linhas)

        # Loop que itera sobre a lista de caminhos de arquivos nos quais será realizada a pesquisa.
        with open(caminho, "r") as arquivo:
            dados = list(DictReader(arquivo))

            # Loop que itera sobre os nomes a serem buscados.
            for nome in lista_nomes:
                print("\tProcurando por \"{}\" no arquivo...".format(nome))
                resultado = pesquisa_sequencial.pesquisa_sequencial(dados, nome)
                if resultado >= 0:
                	print(dictToString(dados[resultado], indent=3))
                	print("\t\tO elemento estava na posição {}.".format(resultado))
                print("")

        print("\n{}".format("-"*comprimento_linhas))


    #================================================================================
    # Parte da pesquisa binária
    #================================================================================
    print("="*comprimento_linhas)
    print("\tPESQUISA BINÁRIA")
    print("="*comprimento_linhas)

    # Loop que itera sobre a lista de caminhos de arquivos nos quais será realizada a pesquisa.
    for caminho in lista_caminhos:

        print("\tRealizando pesquisas no arquivo \"{}\"...".format(caminho))
        print("-"*comprimento_linhas)

        with open(caminho, "r") as arquivo:
            dados = list(DictReader(arquivo))

            # Loop que itera sobre os nomes a serem buscados.
            for nome in lista_nomes:
                print("\tProcurando por \"{}\" no arquivo...".format(nome))
                resultado = pesquisa_binaria.pesquisa_binaria(dados, nome)
                if resultado >= 0:
                	print(dictToString(dados[resultado], indent=3))
                	print("\t\tO elemento estava na posição {}.".format(resultado))
                print("")

        print("\n{}".format("-"*comprimento_linhas))

def dictToString(dictionary, indent=0):
	leading = "\t"*indent
	string = ""

	for key, value in dictionary.items():
		string += "{}{}: \"{}\"".format(leading, key, value)

		if key != list(dictionary.keys())[-1]:
			string += "\n"

	return string


if __name__ == "__main__":
    main()