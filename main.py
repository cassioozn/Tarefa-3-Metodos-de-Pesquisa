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

		for(nome in base_nomes)):

		with open("/1000/crescente_1000.csv") as file:
			data = list(DictReader(file))
			pesquisa_sequencial(data, "Abbey")



if __name__ == "__main__":
	main()