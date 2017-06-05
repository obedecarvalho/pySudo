#!/usr/bin/python2
# -*- coding: utf-8 -*-
'''
Obede
'''

class Casa():
	def __init__(self, valor = 0, imutavel = False):
		self.__valor = int(valor)
		self.__imutavel = bool(imutavel)
		self.__possibilidades = []
		
	def getValor(self):
		return self.__valor
		
	def getImutavel(self):
		return self.__imutavel
		
	def getPossibilidades(self):
		return self.__possibilidades
		
	def setImutavel(self):
		self.__imutavel = True
		
	def setPossibilidades(self, possibilidades = []):
		if not self.__imutavel:
			self.__possibilidades = possibilidades
			return True
		return False
		
	def setValor(self, valor = 0):
		if not self.__imutavel:
			self.__valor = int(valor)
			return True
		return False
		
	def removerPossibilidade (self, possibilidade = 0):
		if possibilidade in self.__possibilidades:
			self.__possibilidades.remove(possibilidade)
			return True
		return False
		
if __name__ == "__main__":
	print ("Classe Casa:  Define a casa do sudoku")
