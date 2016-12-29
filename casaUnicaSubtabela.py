#!/usr/bin/python2
# -*- coding: utf-8 -*-

#from casaUnicaLinha import CasaUnicaLinha
#from casaUnicaColuna import CasaUnicaColuna
from casaUnica import CasaUnica
from tabuleiroCasaUnica import TabuleiroCasaUnica
from controleTabuleiro import ControleTabuleiro

class CasaUnicaSubtabela(CasaUnica):
	
	def __init__(self):
		pass
		
	def calcularPossibilidadesSubtabela(self, tabuleiro = TabuleiroCasaUnica()):
		for subtabela in range(9):
			self.__calcularPossibilidadesSubtabelaN(subtabela, tabuleiro)

	def __calcularPossibilidadesSubtabelaN(self, subtabela, tabuleiro = TabuleiroCasaUnica()):
		ctrlTabuleiro = ControleTabuleiro()
		tabela = tabuleiro.getTabela()
		subtabelaPossibilidades = tabuleiro.getPossibilidadesSubtabela()[subtabela]
		inicioLinha, inicioColuna = ctrlTabuleiro.subtabelaToLinhaColuna(subtabela)
		for linha in range(inicioLinha, inicioLinha+3):
			for coluna in range(inicioColuna, inicioColuna+3):
				casa = tabela[linha][coluna]
				for valorPos in casa.getPossibilidades():
					if valorPos in subtabelaPossibilidades:
						subtabelaPossibilidades[valorPos] += 1
					else:
						subtabelaPossibilidades[valorPos] = 1

	def resolverAlgCasaUnicaSubtabela(self, tabuleiro = TabuleiroCasaUnica()):
		alteracao = True
		umAlteracao = False
		while alteracao:
			alteracao = False
			for subtabela in range(9):
				alteracao = alteracao or self.__resolverAlgCasaUnicaSubtabelaN(subtabela, tabuleiro)
			if alteracao:
				umAlteracao = True
		return umAlteracao
				
	def __resolverAlgCasaUnicaSubtabelaN(self, subtabela, tabuleiro = TabuleiroCasaUnica()):
		alteracao = False
		subtabelaPossibilidades = tabuleiro.getPossibilidadesSubtabela()[subtabela]
		for valorPos, qtde in subtabelaPossibilidades.items():
			if qtde == 1:
				print subtabela, valorPos#
				alteracao = True
				self.__setValorSubtabela(valorPos, subtabela, tabuleiro)
				del subtabelaPossibilidades[valorPos]
		return alteracao
				
	def __setValorSubtabela(self, valorPos, subtabela, tabuleiro = TabuleiroCasaUnica()):
		linhaCasaUnica = CasaUnicaLinha()
		colunaCasaUnica = CasaUnicaColuna()
		tabela = tabuleiro.getTabela()
		ctrlTabuleiro = ControleTabuleiro()
		inicioLinha, inicioColuna = ctrlTabuleiro.subtabelaToLinhaColuna(subtabela)
		for linha in range(inicioLinha, inicioLinha+3):
			for coluna in range(inicioColuna, inicioColuna+3):
				casa = tabela[linha][coluna]
				if valorPos in casa.getPossibilidades():
					casa.setValor(valorPos)
					self.atualizarSubtabela(linha, coluna, tabuleiro)
					casa.setPossibilidades([])
					self.atualizarSubtabelaTabela(linha, coluna, valorPos, tabuleiro)
					linhaCasaUnica.atualizarLinha(linha, coluna, tabuleiro)
					linhaCasaUnica.atualizarLinhaTabela(linha, coluna, tabuleiro)
					colunaCasaUnica.atualizarColuna(linha, coluna, tabuleiro)
					colunaCasaUnica.atualizarColunaTabela(linha, coluna, tabuleiro)
					break
				
	def atualizarSubtabela(self, linha, coluna, tabuleiro = TabuleiroCasaUnica()):
		ctrlTabuleiro = ControleTabuleiro()
		subtabela = ctrlTabuleiro.calcularSubtabela(linha, coluna)
		subtabelaPossibilidades = tabuleiro.getPossibilidadesSubtabela()[subtabela]
		casa = tabuleiro.getTabela()[linha][coluna]
		for valorPos in casa.getPossibilidades():
			subtabelaPossibilidades[valorPos] -= 1
	
	def atualizarSubtabelaTabela(self, linha, coluna, valorPos, tabuleiro = TabuleiroCasaUnica()):
		tabela = tabuleiro.getTabela()
		ctrlTabuleiro = ControleTabuleiro()
		subtabela = ctrlTabuleiro.calcularSubtabela(linha, coluna)
		inicioLinha, inicioColuna = ctrlTabuleiro.subtabelaToLinhaColuna(subtabela)
		for linha in range(inicioLinha, inicioLinha+3):
			for coluna in range(inicioColuna, inicioColuna+3):
				casa = tabela[linha][coluna]
				casa.removerPossibilidade(valorPos)
