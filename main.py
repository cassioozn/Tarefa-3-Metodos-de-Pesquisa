# coding: utf-8

from csv import DictReader
from pathlib import Path, PureWindowsPath
from tabulate import tabulate

import pesquisa_binaria
import pesquisa_sequencial
import sys

def main():
    print("PESQUISA SEQUENCIAL")
    print("---------------------------------------------------------------------------------------------")

    with open("Nomes.txt") as base_nomes:
        print("1000 NOMES.\n")
        print("----------------------------------------------------------------------------------------------\n")
        with open("1000/crescente_1000.csv") as file:
            data = list(DictReader(file))
            for nome in base_nomes.readlines():
                print("=============================================================================================\n")
                pesquisa_sequencial.pesquisa_sequencial(data, nome.strip())

    with open("Nomes.txt") as base_nomes:
        print("\n----------------------------------------------------------------------------------------------\n")
        print("2000 NOMES.\n")
        print("----------------------------------------------------------------------------------------------\n")
        with open("2000/crescente_2000.csv") as file:
            data = list(DictReader(file))
            for nome in base_nomes.readlines():
                print("\n============================================================================================\n")
                pesquisa_sequencial.pesquisa_sequencial(data, nome.strip())

    with open("Nomes.txt") as base_nomes:
        with open("3000/crescente_3000.csv") as file:
            print("\n----------------------------------------------------------------------------------------------\n")
            print("3000 NOMES.\n")
            print("----------------------------------------------------------------------------------------------\n")
            data = list(DictReader(file))
            for nome in base_nomes.readlines():
                print("\n============================================================================================\n")
                print("\n\"" + nome.strip() + "\"\n")
                pesquisa_sequencial.pesquisa_sequencial(data, nome.strip())

    with open("Nomes.txt") as base_nomes:
        with open("5000/crescente_5000.csv") as file:
            print("\n----------------------------------------------------------------------------------------------\n")
            print("5000 NOMES.\n")
            print("----------------------------------------------------------------------------------------------\n")
            data = list(DictReader(file))
            for nome in base_nomes.readlines():
                pesquisa_sequencial.pesquisa_sequencial(data, nome.strip())
                print("\n============================================================================================\n")

    print("\n----------------------------------------------------------------------------------------------")
    print("PESQUISA BINÁRIA")
    print("----------------------------------------------------------------------------------------------")

    with open("Nomes.txt") as base_nomes:
        with open("1000/crescente_1000.csv") as file:
            print("1000 NOMES.\n")
            print("----------------------------------------------------------------------------------------------\n")
            data = list(DictReader(file))
            for nome in base_nomes.readlines():
                print("=============================================================================================\n")
                pesquisa_binaria.pesquisa_binaria(data, nome.strip())

    with open("Nomes.txt") as base_nomes:
        with open("2000/crescente_2000.csv") as file:
            print("\n----------------------------------------------------------------------------------------------\n")
            print("2000 NOMES.\n")
            print("----------------------------------------------------------------------------------------------\n")
            data = list(DictReader(file))
            for nome in base_nomes.readlines():
                pesquisa_binaria.pesquisa_binaria(data, nome.strip())
                print("\n============================================================================================\n")

    with open("Nomes.txt") as base_nomes:
        with open("3000/crescente_3000.csv") as file:
            print("\n----------------------------------------------------------------------------------------------\n")
            print("3000 NOMES.\n")
            print("----------------------------------------------------------------------------------------------\n")
            data = list(DictReader(file))
            for nome in base_nomes.readlines():
                pesquisa_binaria.pesquisa_binaria(data, nome.strip())
                print("\n============================================================================================\n")

    with open("Nomes.txt") as base_nomes:
        with open("5000/crescente_5000.csv") as file:
            print("\n----------------------------------------------------------------------------------------------\n")
            print("5000 NOMES.\n")
            print("----------------------------------------------------------------------------------------------\n")
            data = list(DictReader(file))
            for nome in base_nomes.readlines():
                pesquisa_binaria.pesquisa_binaria(data, nome.strip())
                print("\n============================================================================================\n")


if __name__ == "__main__":
    main()