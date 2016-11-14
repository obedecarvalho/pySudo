#!/usr/bin/python2
# -*- coding: utf-8 -*-

class SudokuBD():
	def __init__(self, entrada = 'entrada.txt', saida = 'saida.txt'):
		self.__entrada = open(entrada)
		self.__saida = open(saida, 'w')
		self.cont = 0
		
	def proximo(self):
		return self.__entrada.readline()
		
	def salvar(self, escrever):
		self.cont+=1
		if self.cont == 255:
			self.cont = 0
			self.__saida.flush()
		return self.__saida.write('<'+ escrever +'>\n')
		
	def fechar(self):
		self.__entrada.close()
		self.__saida.flush()
		self.__saida.close()

if __name__ == "__main__":
	print ("Classe Sudoku:  Define o acesso aos dados do sudoku")
