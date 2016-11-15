#!/usr/bin/python2
# -*- coding: utf-8 -*-

from algoritmoResolucao import AlgoritmoResolucao
from tabuleiroCasaUnica import TabuleiroCasaUnica
from controleTabuleiro import ControleTabuleiro

class CasaUnica(AlgoritmoResolucao):
	
	def __init__(self):
		pass
		
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
		umAlteracao = False
		while alteracao:
			alteracao = False
			for linha in range(9):
				alteracaoAtual = self.__resolverAlgCasaUnicaLinhaN(linha, tabuleiro)
				alteracao = alteracao or alteracaoAtual
			if alteracao:
				umAlteracao = True
		return umAlteracao
				
	def __resolverAlgCasaUnicaLinhaN(self, linha, tabuleiro = TabuleiroCasaUnica()):
		alteracao = False
		linhaPossibilidades = tabuleiro.getPossibilidadesLinha()[linha]
		for valorPos, qtde in linhaPossibilidades.items():
			if qtde == 1:
				print 'Linha: ',linha, valorPos#
				alteracao = True
				self.__setValorLinha(valorPos, linha, tabuleiro)
				del linhaPossibilidades[valorPos]
		return alteracao
				
	def __setValorLinha(self, valorPos, linha, tabuleiro = TabuleiroCasaUnica()):
		colunaCasaUnica = CasaUnicaColuna()
		subtabelaCasaUnica = CasaUnicaSubtabela()
		linhaTabela = tabuleiro.getTabela()[linha]
		for coluna in range(9):
			casa = linhaTabela[coluna]
			if valorPos in casa.getPossibilidades():
				casa.setValor(valorPos)
				self.atualizarLinha(linha, coluna, tabuleiro)
				self.atualizarLinhaTabela(linha, coluna, valorPos, tabuleiro)
				colunaCasaUnica.atualizarColuna(linha, coluna, tabuleiro)
				colunaCasaUnica.atualizarColunaTabela(linha, coluna, valorPos, tabuleiro)
				subtabelaCasaUnica.atualizarSubtabela(linha, coluna, tabuleiro)
				subtabelaCasaUnica.atualizarSubtabelaTabela(linha, coluna, valorPos, tabuleiro)
				casa.setPossibilidades([])
				break
				
	def atualizarLinha(self, linha, coluna, tabuleiro = TabuleiroCasaUnica()):
		linhaPossibilidades = tabuleiro.getPossibilidadesLinha()[linha]
		casa = tabuleiro.getTabela()[linha][coluna]
		for valorPos in casa.getPossibilidades():
			linhaPossibilidades[valorPos] -= 1
	
	def atualizarLinhaTabela(self, linha, coluna, valorPos, tabuleiro = TabuleiroCasaUnica()):
		linhaTabela = tabuleiro.getTabela()[linha]
		for casa in linhaTabela:
			casa.removerPossibilidade(valorPos)

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
		umAlteracao = False
		while alteracao:
			alteracao = False
			for coluna in range(9):
				alteracaoAtual = self.__resolverAlgCasaUnicaColunaN(coluna, tabuleiro)
				alteracao = alteracao or alteracaoAtual
			if alteracao:
				umAlteracao = True
		return umAlteracao
				
	def __resolverAlgCasaUnicaColunaN(self, coluna, tabuleiro = TabuleiroCasaUnica()):
		alteracao = False
		colunaPossibilidades = tabuleiro.getPossibilidadesColuna()[coluna]
		for valorPos, qtde in colunaPossibilidades.items():
			if qtde == 1:
				print 'Coluna: ',coluna, valorPos#
				alteracao = True
				self.__setValorColuna(valorPos, coluna, tabuleiro)
				del colunaPossibilidades[valorPos]
		return alteracao
				
	def __setValorColuna(self, valorPos, coluna, tabuleiro = TabuleiroCasaUnica()):
		linhaCasaUnica = CasaUnicaLinha()
		subtabelaCasaUnica = CasaUnicaSubtabela()
		tabela = tabuleiro.getTabela()
		for linha in range(9):
			casa = tabela[linha][coluna]
			if valorPos in casa.getPossibilidades():
				casa.setValor(valorPos)
				self.atualizarColuna(linha, coluna, tabuleiro)
				self.atualizarColunaTabela(linha, coluna, valorPos, tabuleiro)
				linhaCasaUnica.atualizarLinha(linha, coluna, tabuleiro)
				linhaCasaUnica.atualizarLinhaTabela(linha, coluna, valorPos, tabuleiro)
				subtabelaCasaUnica.atualizarSubtabela(linha, coluna, tabuleiro)
				subtabelaCasaUnica.atualizarSubtabelaTabela(linha, coluna, valorPos,tabuleiro)
				casa.setPossibilidades([])
				break
				
	def atualizarColuna(self, linha, coluna, tabuleiro = TabuleiroCasaUnica()):
		colunaPossibilidades = tabuleiro.getPossibilidadesColuna()[coluna]
		casa = tabuleiro.getTabela()[linha][coluna]
		for valorPos in casa.getPossibilidades():
			colunaPossibilidades[valorPos] -= 1
	
	def atualizarColunaTabela(self, linha, coluna, valorPos, tabuleiro = TabuleiroCasaUnica()):
		tabela = tabuleiro.getTabela()
		for linha in range(9):
			casa = tabela[linha][coluna]
			casa.removerPossibilidade(valorPos)

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
				alteracaoAtual = self.__resolverAlgCasaUnicaSubtabelaN(subtabela, tabuleiro)
				alteracao = alteracao or alteracaoAtual
			if alteracao:
				umAlteracao = True
		return umAlteracao
				
	def __resolverAlgCasaUnicaSubtabelaN(self, subtabela, tabuleiro = TabuleiroCasaUnica()):
		alteracao = False
		subtabelaPossibilidades = tabuleiro.getPossibilidadesSubtabela()[subtabela]
		for valorPos, qtde in subtabelaPossibilidades.items():
			if qtde == 1:
				print 'Subtabela: ',subtabela, valorPos#
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
					self.atualizarSubtabelaTabela(linha, coluna, valorPos, tabuleiro)
					linhaCasaUnica.atualizarLinha(linha, coluna, tabuleiro)
					linhaCasaUnica.atualizarLinhaTabela(linha, coluna,valorPos, tabuleiro)
					colunaCasaUnica.atualizarColuna(linha, coluna, tabuleiro)
					colunaCasaUnica.atualizarColunaTabela(linha, coluna,valorPos, tabuleiro)
					casa.setPossibilidades([])
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
