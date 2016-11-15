#!/usr/bin/python2
# -*- coding: utf-8 -*-

from casaUnica import CasaUnica
from tabuleiroCasaUnica import TabuleiroCasaUnica

class CasaUnicaColuna(CasaUnica):
	
	def __init__(self):
		pass
		
	def calcularPossibilidadesColuna(self, tabuleiro = TabuleiroCasaUnica()):
		for coluna in range(9):
			self.__calcularPossibilidadesColunaN(coluna, tabuleiro)

	def __calcularPossibilidadesColunaN(self, coluna, tabuleiro = TabuleiroCasaUnica()):
		tabela = tabuleiro.getTabela()
		colunaPossibilidades = tabuleiro.getPossibilidadesColuna()[coluna]
		for linha in range(9):
			casa = tabela[linha][coluna]
			for valorPos in casa.getPossibilidades():
				if valorPos in colunaPossibilidades:
					colunaPossibilidades[valorPos] += 1
				else:
					colunaPossibilidades[valorPos] = 1

	def resolverAlgCasaUnicaColuna(self, tabuleiro = TabuleiroCasaUnica()):
		alteracao = True
		while alteracao:
			alteracao = False
			for coluna in range(9):
				alteracao = alteracao or self.__resolverAlgCasaUnicaColunaN(coluna, tabuleiro)
				
	def __resolverAlgCasaUnicaColunaN(self, coluna, tabuleiro = TabuleiroCasaUnica()):
		alteracao = False
		colunaPossibilidades = tabuleiro.getPossibilidadesColuna()[coluna]
		for valorPos, qtde in colunaPossibilidades.items():
			if qtde == 1:
				alteracao = True
				self.__setValorColuna(valorPos, coluna, tabuleiro)
				del colunaPossibilidades[valorPos]
		return alteracao
				
	def __setValorColuna(self, valorPos, coluna, tabuleiro = TabuleiroCasaUnica()):
		tabela = tabuleiro.getTabela()
		for linha in range(9):
			casa = tabela[linha][coluna]
			if valorPos in casa.getPossibilidades():
				casa.setValor(valorPos)
				self.__atualizarColuna(linha, coluna, tabuleiro)
				casa.setPossibilidades([])
				self.__atualizarColunaTabela(linha, coluna, valorPos, tabuleiro)
				break
				
	def __atualizarColuna(self, linha, coluna, tabuleiro = TabuleiroCasaUnica()):
		colunaPossibilidades = tabuleiro.getPossibilidadesColuna()[coluna]
		casa = tabuleiro.getTabela()[linha][coluna]
		for valorPos in casa.getPossibilidades():
			colunaPossibilidades[valorPos] -= 1
	
	def __atualizarColunaTabela(self, linha, coluna, valorPos, tabuleiro = TabuleiroCasaUnica()):
		tabela = tabuleiro.getTabela()
		for linha in range(9):
			casa = tabela[linha][coluna]
			casa.removerPossibilidade(valorPos)
