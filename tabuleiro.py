#!/usr/bin/python2
# -*- coding: utf-8 -*-

from casa import Casa

class Tabuleiro():
	def __init__(self):
		self.__tabela = []
		self.__tamanhoTabela = 81
		for linha in range(9):
			self.__tabela.append([])
			for coluna in range(9):
				self.__tabela[linha].append(Casa())
				
	def getTabela(self):
		return self.__tabela
		
	def setCasa(self, linha, coluna, valor = 0):
		return self.__tabela[linha][coluna].setValor(valor)
	
	def setTabela(self, novaTabela = ''):
		tabela_bk = []
		if not novaTabela:
			novaTabela = '0'*self.__tamanhoTabela
		tabela_bk [:] = self.__tabela
		valido = True
		if len(novaTabela) == self.__tamanhoTabela:
			for i in range(len(novaTabela)):
				valido = valido and self.__tabela[i//9][i%9].setValor(novaTabela[i])
				if novaTabela[i] != '0':
					self.__tabela[i//9][i%9].setImutavel()
				
		else:
			return False
		if valido:
			return True
		else:
			self.__tabela [:] = tabela_bk
			return False
			
	def salvarString(self):
		stringValores = []
		for linha in self.__tabela:
			for casa in linha:
				stringValores.append(str(casa.getValor()))
		return ''.join(stringValores)
		
if __name__ == "__main__":
	print ("Classe Tabuleiro:  Define o tabuleiro do sudoku")
