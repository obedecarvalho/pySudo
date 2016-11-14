#!/usr/bin/python2
# -*- coding: utf-8 -*-

from casa import Casa
from tabuleiro import Tabuleiro

class ControleTabuleiro():

	def __init__(self):
		pass

	def calcularSubtabela(self, linha, coluna):
		return (int((linha//3) * 3 + coluna//3))

	def subtabelaToLinhaColuna(self,subtabela):
		inicioLinha = int(((subtabela)//3)*3)
		inicioColuna = int(((subtabela)%3)*3)
		return (inicioLinha, inicioColuna)

	def casaValida(self, linha, coluna, tabuleiro = Tabuleiro()):
		subtabela = self.calcularSubtabela(linha, coluna)
		return (self.__linhaValida(linha, tabuleiro) and self.__colunaValida(coluna, tabuleiro) and self.__subtabelaValida(subtabela, tabuleiro))

	def __linhaValida(self, linha, tabuleiro):
		valores = []
		for casa in tabuleiro.getTabela()[linha]:
			valor = casa.getValor()
			if valor == 0:
				continue
			elif valor in valores:
				return False
			else:
				valores.append(valor)
		return True

	def __colunaValida(self, coluna, tabuleiro):
		valores = []
		tabela = tabuleiro.getTabela()
		for linha in range(9):
			valor = tabela[linha][coluna].getValor()
			if valor == 0:
				continue
			elif  valor in valores:
				return False
			else:
				valores.append(valor)
		return True

	def __subtabelaValida(self,subtabela, tabuleiro):
		valoresExistentes = []
		tabela = tabuleiro.getTabela()
		inicioLinha, inicioColuna = self.subtabelaToLinhaColuna(subtabela)
		for linha in range(inicioLinha, inicioLinha+3):
			for coluna in range(inicioColuna, inicioColuna+3):
				valor = tabela[linha][coluna].getValor()
				if valor == 0:
					continue
				elif valor in valoresExistentes:
					return False
				elif valor != 0:
					valoresExistentes.append(valor)
		return  True

	def tabelaCompleta(self, tabuleiro = Tabuleiro()):
		finalizada = True
		for linha in tabuleiro.getTabela():
			for casa in linha:
				if casa.getValor == 0:
					finalizada = False
		return finalizada

	def tabelaValida(self, tabuleiro = Tabuleiro()):
		valida = True
		for linha in range(9):
			valida = valida and self.__linhaValida(linha, tabuleiro)
			if not valida:
				return False
		for coluna in range(9):
			valida = valida and self.__colunaValida(coluna, tabuleiro)
			if not valida:
				return False
		for subtabela in range(9):
			valida = valida and self.__subtabelaValida(subtabela, tabuleiro)
			if not valida:
				return False
		return valida

	def mostrarTabela(self, tabuleiro = Tabuleiro()):
		print ('\n')
		sudoku = tabuleiro.salvarString()
		linhas = []
		for i in range(9):
			linhas.append(sudoku[i*9:i*9+9])
		sep = '|'
		for lin in linhas:
			print (sep.join(lin))

	def mostrarPossibilidades(self, tabuleiro = Tabuleiro()):
		tabela = tabuleiro.getTabela()
		for linha in range(9):
			for coluna in range(9):
				casa = tabela[linha][coluna]
				print (linha, coluna, casa.getPossibilidades())

if __name__ == "__main__":
	print ("Classe ControleTabuleiro:  Define o controle do tabuleiro do sudoku")
