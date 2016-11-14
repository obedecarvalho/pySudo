#!/usr/bin/python2
# -*- coding: utf-8 -*-


from tabuleiro import Tabuleiro
from calcularPossibilidadeCasa import CalcularPossibilidadeCasa
from possibilidadeUnica import PossibilidadeUnica
from controleTabuleiro import ControleTabuleiro

#from casa import Casa
#from algoritmoResolucao import AlgoritmoResolucao
#from extencaoControlador import ExtencaoControlador
#from controleTabuleiro import ControleTabuleiro

class Simulador():
	def __init__(self):
		pass

	def __calcularPossibilidades(self, tabuleiro = Tabuleiro()):
		calcularPossibilidade = CalcularPossibilidadeCasa()
		calcularPossibilidade.calcularPossibilidades(tabuleiro)
		return
				
	def __resolverAlgPossibilidadeUnica(self, tabuleiro = Tabuleiro()):
		algPossibilidadeUnica = PossibilidadeUnica()
		algPossibilidadeUnica.resolverPossibilidadeUnica(tabuleiro)
		return
				
	def run (self, tabuleiro = Tabuleiro()):
		controlador = ControleTabuleiro()
		self.__calcularPossibilidades(tabuleiro)
		controlador.mostrarPossibilidades(tabuleiro)#
		self.__resolverAlgPossibilidadeUnica(tabuleiro)
		controlador.mostrarTabela(tabuleiro)#
		return tabuleiro.salvarString()
			
	'''
	def run2(self):
		self.__calcularPossibilidadesTodos()
		self.__controlador.mostrarTabela(self.__tabuleiros[0])
		self.__controlador.mostrarPossibilidades(self.__tabuleiros[0])
		c = ExtencaoControlador()
		c.calcularPossibilidades(self.__tabuleiros[0])
		c.resolverPossibilidades(self.__tabuleiros[0])
		self.__controlador.mostrarTabela(self.__tabuleiros[0])
		
		if len(self.__tabuleiros) > 0:
			self.__controlador.mostrarTabela(self.__tabuleiros[0])
			if self.__controlador.tabelaValida(self.__tabuleiros[0]):
				return self.__tabuleiros[0].salvarString()
			else:
				return '0x00 - error'
		else:
			return '0x00 - error'
		
	'''

if __name__ == "__main__":
	print ("Classe Simulador: Define o simulador do sudoku")
