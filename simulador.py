#!/usr/bin/python2
# -*- coding: utf-8 -*-

from tabuleiro import Tabuleiro
from tabuleiroCasaUnica import TabuleiroCasaUnica
from calcularPossibilidadeCasa import CalcularPossibilidadeCasa
from possibilidadeUnica import PossibilidadeUnica
from controleTabuleiro import ControleTabuleiro
from visualizador import Visualizador
from casaUnica import CasaUnicaLinha
from casaUnica import CasaUnicaColuna
from casaUnica import CasaUnicaSubtabela

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
		
	def __resolverAlgCasaUnica(self, tabuleiro = TabuleiroCasaUnica()):
		algoritmoCasaUnicaLinha = CasaUnicaLinha()
		algoritmoCasaUnicaSubtabela = CasaUnicaSubtabela()
		algoritmoCasaUnicaColuna = CasaUnicaColuna()
		alteracao = True
		while alteracao:
			alteracao = False
			umaAlteracao = algoritmoCasaUnicaLinha.resolverAlgCasaUnicaLinha(tabuleiro)
			alteracao = alteracao or umaAlteracao
			umaAlteracao = algoritmoCasaUnicaColuna.resolverAlgCasaUnicaColuna(tabuleiro)
			alteracao = umaAlteracao or alteracao
			algoritmoCasaUnicaSubtabela.resolverAlgCasaUnicaSubtabela(tabuleiro)
			alteracao = umaAlteracao or alteracao
				
	def run (self, tabuleiro = Tabuleiro()):
		vizu = Visualizador()
		self.__calcularPossibilidades(tabuleiro)
		vizu.mostrarPossibilidades(tabuleiro)#
		self.__resolverAlgPossibilidadeUnica(tabuleiro)
		vizu.mostrarTabela(tabuleiro)#
		return tabuleiro.salvarString()
		
	def run5 (self, tabuleiro = TabuleiroCasaUnica()):
		print '-'*50
		vizu = Visualizador()
		vizu.mostrarTabela(tabuleiro)#
		self.__calcularPossibilidades(tabuleiro)
		self.__calcularPossibilidadesLinha(tabuleiro)
		self.__calcularPossibilidadesColuna(tabuleiro)
		self.__calcularPossibilidadesSubtabela(tabuleiro)
		vizu.mostrarPossibilidadesLinha(tabuleiro)#
		vizu.mostrarPossibilidadesColuna(tabuleiro)#
		vizu.mostrarPossibilidadesSubtabela(tabuleiro)#
		self.__resolverAlgCasaUnica(tabuleiro)
		vizu.mostrarTabela(tabuleiro)#
		vizu.mostrarPossibilidadesLinha(tabuleiro)#
		vizu.mostrarPossibilidadesColuna(tabuleiro)#
		vizu.mostrarPossibilidadesSubtabela(tabuleiro)#
		return tabuleiro.salvarString()
		
	
	def run2 (self, tabuleiro = TabuleiroCasaUnica()):
		print '-'*50
		vizu = Visualizador()
		vizu.mostrarTabela(tabuleiro)#
		self.__calcularPossibilidades(tabuleiro)
		self.__calcularPossibilidadesLinha(tabuleiro)
		self.__calcularPossibilidadesColuna(tabuleiro)#
		self.__calcularPossibilidadesSubtabela(tabuleiro)#
		vizu.mostrarPossibilidadesLinha(tabuleiro)#
		self.__resolverAlgCasaUnicaLinha(tabuleiro)
		vizu.mostrarTabela(tabuleiro)#
		vizu.mostrarPossibilidadesLinha(tabuleiro)#
		return tabuleiro.salvarString()
		
	def run3 (self, tabuleiro = TabuleiroCasaUnica()):
		vizu = Visualizador()
		vizu.mostrarTabela(tabuleiro)#
		self.__calcularPossibilidades(tabuleiro)
		self.__calcularPossibilidadesLinha(tabuleiro)#
		self.__calcularPossibilidadesColuna(tabuleiro)
		self.__calcularPossibilidadesSubtabela(tabuleiro)#
		vizu.mostrarPossibilidadesColuna(tabuleiro)#
		self.__resolverAlgCasaUnicaColuna(tabuleiro)
		vizu.mostrarTabela(tabuleiro)#
		vizu.mostrarPossibilidadesColuna(tabuleiro)#
		return tabuleiro.salvarString()
		
	def run4 (self, tabuleiro = TabuleiroCasaUnica()):
		vizu = Visualizador()
		vizu.mostrarTabela(tabuleiro)#
		self.__calcularPossibilidades(tabuleiro)
		self.__calcularPossibilidadesLinha(tabuleiro)#
		self.__calcularPossibilidadesColuna(tabuleiro)#
		self.__calcularPossibilidadesSubtabela(tabuleiro)
		vizu.mostrarPossibilidadesSubtabela(tabuleiro)#
		self.__resolverAlgCasaUnicaSubtabela(tabuleiro)
		vizu.mostrarTabela(tabuleiro)#
		vizu.mostrarPossibilidadesSubtabela(tabuleiro)#
		return tabuleiro.salvarString()
			
if __name__ == "__main__":
	print ("Classe Simulador: Define o simulador do sudoku")
