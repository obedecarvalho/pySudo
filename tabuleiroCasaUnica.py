#!/usr/bin/python2
# -*- coding: utf-8 -*-

from casa import Casa
from tabuleiro import Tabuleiro

class TabuleiroCasaUnica(Tabuleiro):
	
	def __init__(self):
		Tabuleiro.__init__(self)
		self.__possibilidadesLinha = []		
		self.__possibilidadesColuna = []		
		self.__possibilidadesSubtabela = []
		self.__inicializarPossibilidades(self.__possibilidadesLinha)
		self.__inicializarPossibilidades(self.__possibilidadesColuna)
		self.__inicializarPossibilidades(self.__possibilidadesSubtabela)
		
	def __inicializarPossibilidades(self, possibilidades):
		for i in range(9):
			possibilidades.append({})
	
	def getPossibilidadesLinha(self):
		return self.__possibilidadesLinha
		
	def getPossibilidadesColuna(self):
		return self.__possibilidadesColuna
		
	def getPossibilidadesSubtabela(self):
		return self.__possibilidadesSubtabela
