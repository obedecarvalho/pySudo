#!/usr/bin/python2
# -*- coding: utf-8 -*-

from casa import Casa
from tabuleiro import Tabuleiro
from controleTabuleiro import ControleTabuleiro

class CalcularPossibilidadeCasa():

	def __init__(self):
		self.__ctrlTabuleiro = ControleTabuleiro()

	def calcularPossibilidades(self, tabuleiro = Tabuleiro()):
		for linha in range(9):
			for coluna in range(9):
				casa = tabuleiro.getTabela()[linha][coluna]
				if casa.getValor() == 0:
					self.__calcularPossibilidadesCasa(linha,coluna,tabuleiro)
		return

	def __calcularPossibilidadesCasa(self, linha, coluna,  tabuleiro = Tabuleiro()):
		possibilidades = []
		casa = tabuleiro.getTabela()[linha][coluna]
		for valor in range(1,10):
			casa.setValor(valor)
			if self.__ctrlTabuleiro.casaValida(linha,coluna, tabuleiro):
				possibilidades.append(valor)
		casa.setValor(0)
		casa.setPossibilidades(possibilidades)
		return

if __name__ == "__main__":
	print ("Classe .. do sudoku")
