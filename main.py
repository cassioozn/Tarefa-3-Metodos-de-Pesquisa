# coding: utf-8

from csv import DictReader
from pathlib import Path, PureWindowsPath
from tabulate import tabulate

import pesquisa_binaria
import pesquisa_sequencial


def main():
    print("PESQUISA SEQUENCIAL")
    print("---------------------------------------------------------------------------------------------")

    with open("Nomes.txt") as base_nomes:
        for nome in base_nomes.readlines():
            with open("/1000/crescente_1000.csv") as file:
                data = list(DictReader(file))
                pesquisa_sequencial.pesquisa_sequencial(data, nome)
                print("---------------------------------------------------------------------------------------------")

        for nome in base_nomes.readlines():
            with open("/2000/crescente_2000.csv") as file:
                data = list(DictReader(file))
                pesquisa_sequencial.pesquisa_sequencial(data, nome)
                print("---------------------------------------------------------------------------------------------")

        for nome in base_nomes.readlines():
            with open("/3000/crescente_3000.csv") as file:
                data = list(DictReader(file))
                pesquisa_sequencial.pesquisa_sequencial(data, nome)
                print("---------------------------------------------------------------------------------------------")

        for nome in base_nomes.readlines():
            with open("/5000/crescente_5000.csv") as file:
                data = list(DictReader(file))
                pesquisa_sequencial.pesquisa_sequencial(data, nome)
                print("---------------------------------------------------------------------------------------------")

        print("PESQUISA BINÁRIA")
        print("---------------------------------------------------------------------------------------------")

        for nome in base_nomes.readlines():
            with open("/1000/crescente_1000.csv") as file:
                data = list(DictReader(file))
                pesquisa_binaria.pesquisa_binaria(data, nome)
                print("---------------------------------------------------------------------------------------------")

        for nome in base_nomes.readlines():
            with open("/2000/crescente_2000.csv") as file:
                data = list(DictReader(file))
                pesquisa_binaria.pesquisa_binaria(data, nome)
                print("---------------------------------------------------------------------------------------------")

        for nome in base_nomes.readlines():
            with open("/3000/crescente_3000.csv") as file:
                data = list(DictReader(file))
                pesquisa_binaria.pesquisa_binaria(data, nome)
                print("---------------------------------------------------------------------------------------------")

        for nome in base_nomes.readlines():
            with open("/5000/crescente_5000.csv") as file:
                data = list(DictReader(file))
                pesquisa_binaria.pesquisa_binaria(data, nome)
                print("---------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()