#!/usr/bin/python2
# -*- coding: utf-8 -*-

from casa import Casa
from tabuleiro import Tabuleiro
from controleTabuleiro import ControleTabuleiro
from algoritmoResolucao import AlgoritmoResolucao

class PossibilidadeUnica(AlgoritmoResolucao):

	def __init__(self):
		pass
		
	def __resolverPossibilidadeUnicaCasa(self, linha, coluna, tabuleiro = Tabuleiro()):		
		alteracao = False
		casa = tabuleiro.getTabela()[linha][coluna]
		possibilidades = casa.getPossibilidades()
		if len(possibilidades) == 1 and casa.getValor() == 0:
			alteracao = True
			casa.setValor(possibilidades[0])
			self.__removerPossibilidadeResolvida(linha, coluna, possibilidades[0], tabuleiro)
		return alteracao

	def resolverPossibilidadeUnica(self, tabuleiro = Tabuleiro()):
		alteracao = True
		while alteracao:
			alteracao = False
			for linha in range(9):
				for coluna in range(9):
					alteracao = alteracao or self.__resolverPossibilidadeUnicaCasa(linha, coluna, tabuleiro)
		return

	def __removerPossibilidadeResolvida(self, linha, coluna, possibilidade, tabuleiro = Tabuleiro):
		ctrlTabuleiro = ControleTabuleiro()
		self.__removerPossibilidadeResolvidaLinha(linha, possibilidade, tabuleiro)
		self.__removerPossibilidadeResolvidaColuna(coluna, possibilidade, tabuleiro)
		subtabela = ctrlTabuleiro.calcularSubtabela(linha,coluna)
		self.__removerPossibilidadeResolvidaSubtabela(subtabela, possibilidade, tabuleiro)

	def __removerPossibilidadeResolvidaLinha(self, linha, possibilidade, tabuleiro = Tabuleiro()):
		tabela = tabuleiro.getTabela()
		for casa in tabela[linha]:
			casa.removerPossibilidade(possibilidade)

	def __removerPossibilidadeResolvidaColuna(self, coluna, possibilidade, tabuleiro = Tabuleiro()):
		tabela = tabuleiro.getTabela()
		for lin in range(9):
			tabela[lin][coluna].removerPossibilidade(possibilidade)
			
	def __removerPossibilidadeResolvidaSubtabela(self, subtabela, possibilidade, tabuleiro = Tabuleiro()):
		ctrlTabuleiro = ControleTabuleiro()
		tabela = tabuleiro.getTabela()
		linha_inicio, coluna_inicio = ctrlTabuleiro.subtabelaToLinhaColuna(subtabela)
		for lin in range(linha_inicio, linha_inicio+3):
			for col in range(coluna_inicio, coluna_inicio+3):
				tabela[lin][col].removerPossibilidade(possibilidade)

if __name__ == "__main__":
	print ("Classe .. do sudoku")
