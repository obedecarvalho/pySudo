#!/usr/bin/python2
# -*- coding: utf-8 -*-

from tabuleiro import Tabuleiro
from tabuleiroCasaUnica import TabuleiroCasaUnica
from calcularPossibilidadeCasa import CalcularPossibilidadeCasa
from possibilidadeUnica import PossibilidadeUnica
from controleTabuleiro import ControleTabuleiro
from visualizador import Visualizador
from casaUnicaLinha import CasaUnicaLinha
from casaUnicaColuna import CasaUnicaColuna
from casaUnicaSubtabela import CasaUnicaSubtabela

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
		
	def __calcularPossibilidadesColuna(self, tabuleiro = TabuleiroCasaUnica()):
		algoritmoCasaUnica = CasaUnicaColuna()
		algoritmoCasaUnica.calcularPossibilidadesColuna(tabuleiro)
		return
		
	def __resolverAlgCasaUnicaColuna(self, tabuleiro = TabuleiroCasaUnica()):
		algoritmoCasaUnica = CasaUnicaColuna()
		algoritmoCasaUnica.resolverAlgCasaUnicaColuna(tabuleiro)
		return
	
	def __calcularPossibilidadesSubtabela(self, tabuleiro = TabuleiroCasaUnica()):
		algoritmoCasaUnica = CasaUnicaSubtabela()
		algoritmoCasaUnica.calcularPossibilidadesSubtabela(tabuleiro)
		return
		
	def __resolverAlgCasaUnicaSubtabela(self, tabuleiro = TabuleiroCasaUnica()):
		algoritmoCasaUnica = CasaUnicaSubtabela()
		algoritmoCasaUnica.resolverAlgCasaUnicaSubtabela(tabuleiro)
		return
		
	def __calcularPossibilidadesLinha(self, tabuleiro = TabuleiroCasaUnica()):
		algoritmoCasaUnica = CasaUnicaLinha()
		algoritmoCasaUnica.calcularPossibilidadesLinha(tabuleiro)
		return
		
	def __resolverAlgCasaUnicaLinha(self, tabuleiro = TabuleiroCasaUnica()):
		algoritmoCasaUnica = CasaUnicaLinha()
		algoritmoCasaUnica.resolverAlgCasaUnicaLinha(tabuleiro)
		return
				
	def run (self, tabuleiro = Tabuleiro()):
		vizu = Visualizador()
		self.__calcularPossibilidades(tabuleiro)
		vizu.mostrarPossibilidades(tabuleiro)#
		self.__resolverAlgPossibilidadeUnica(tabuleiro)
		vizu.mostrarTabela(tabuleiro)#
		return tabuleiro.salvarString()
		
	def run2 (self, tabuleiro = TabuleiroCasaUnica()):
		vizu = Visualizador()
		vizu.mostrarTabela(tabuleiro)#
		self.__calcularPossibilidades(tabuleiro)
		self.__calcularPossibilidadesLinha(tabuleiro)
		vizu.mostrarPossibilidadesLinha(tabuleiro)#
		self.__resolverAlgCasaUnicaLinha(tabuleiro)
		vizu.mostrarTabela(tabuleiro)#
		vizu.mostrarPossibilidadesLinha(tabuleiro)#
		return tabuleiro.salvarString()
		
	def run3 (self, tabuleiro = TabuleiroCasaUnica()):
		vizu = Visualizador()
		vizu.mostrarTabela(tabuleiro)#
		self.__calcularPossibilidades(tabuleiro)
		self.__calcularPossibilidadesColuna(tabuleiro)
		vizu.mostrarPossibilidadesColuna(tabuleiro)#
		self.__resolverAlgCasaUnicaColuna(tabuleiro)
		vizu.mostrarTabela(tabuleiro)#
		vizu.mostrarPossibilidadesColuna(tabuleiro)#
		return tabuleiro.salvarString()
		
	def run4 (self, tabuleiro = TabuleiroCasaUnica()):
		vizu = Visualizador()
		vizu.mostrarTabela(tabuleiro)#
		self.__calcularPossibilidades(tabuleiro)
		self.__calcularPossibilidadesSubtabela(tabuleiro)
		vizu.mostrarPossibilidadesSubtabela(tabuleiro)#
		self.__resolverAlgCasaUnicaSubtabela(tabuleiro)
		vizu.mostrarTabela(tabuleiro)#
		vizu.mostrarPossibilidadesSubtabela(tabuleiro)#
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
