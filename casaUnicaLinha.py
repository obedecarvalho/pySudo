#!/usr/bin/python2
# -*- coding: utf-8 -*-

from casaUnica import CasaUnica
from casa import Casa
from tabuleiroCasaUnica import TabuleiroCasaUnica

class CasaUnicaLinha(CasaUnica):
	
	def __init__(self):
		pass
		
	def calcularPossibilidadesLinha(self, tabuleiro = TabuleiroCasaUnica()):
		for linha in range(9):
			self.__calcularPossibilidadesLinhaN(linha, tabuleiro)

	def __calcularPossibilidadesLinhaN(self, linha, tabuleiro = TabuleiroCasaUnica()):
		linhaTabela = tabuleiro.getTabela()[linha]
		linhaPossibilidades = tabuleiro.getPossibilidadesLinha()[linha]
		for casa in linhaTabela:
			for valorPos in casa.getPossibilidades():
				if valorPos in linhaPossibilidades:
					linhaPossibilidades[valorPos] += 1
				else:
					linhaPossibilidades[valorPos] = 1

	def resolverAlgCasaUnicaLinha(self, tabuleiro = TabuleiroCasaUnica()):
		alteracao = True
		while alteracao:
			alteracao = False
			for linha in range(9):
				alteracao = alteracao or self.__resolverAlgCasaUnicaLinhaN(linha, tabuleiro)
				
	def __resolverAlgCasaUnicaLinhaN(self, linha, tabuleiro = TabuleiroCasaUnica()):
		alteracao = False
		linhaPossibilidades = tabuleiro.getPossibilidadesLinha()[linha]
		for valorPos, qtde in linhaPossibilidades.items():
			if qtde == 1:
				alteracao = True
				self.__setValorLinha(valorPos, linha, tabuleiro)
				del linhaPossibilidades[valorPos]
		return alteracao
				
	def __setValorLinha(self, valorPos, linha, tabuleiro = TabuleiroCasaUnica()):
		linhaTabela = tabuleiro.getTabela()[linha]
		for coluna in range(9):
			casa = linhaTabela[coluna]
			if valorPos in casa.getPossibilidades():
				casa.setValor(valorPos)
				self.__atualizarLinha(linha, coluna, tabuleiro)
				casa.setPossibilidades([])
				self.__atualizarLinhaTabela(linha, coluna, valorPos, tabuleiro)
				break
				
	def __atualizarLinha(self, linha, coluna, tabuleiro = TabuleiroCasaUnica()):
		linhaPossibilidades = tabuleiro.getPossibilidadesLinha()[linha]
		casa = tabuleiro.getTabela()[linha][coluna]
		for valorPos in casa.getPossibilidades():
			linhaPossibilidades[valorPos] -= 1
	
	def __atualizarLinhaTabela(self, linha, coluna, valorPos, tabuleiro = TabuleiroCasaUnica()):
		linhaTabela = tabuleiro.getTabela()[linha]
		for casa in linhaTabela:
			casa.removerPossibilidade(valorPos)
