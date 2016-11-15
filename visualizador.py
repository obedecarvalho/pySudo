#!/usr/bin/python2
# -*- coding: utf-8 -*-

from tabuleiro import Tabuleiro
from tabuleiroCasaUnica import TabuleiroCasaUnica

class Visualizador():
	def __init__(self):
		pass
		
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
		print ('\n')
		tabela = tabuleiro.getTabela()
		for linha in range(9):
			for coluna in range(9):
				casa = tabela[linha][coluna]
				print (linha, coluna, casa.getPossibilidades())
				
	def mostrarPossibilidadesLinha(self, tabuleiro = TabuleiroCasaUnica()):
		print ('\n')
		linhas = tabuleiro.getPossibilidadesLinha()
		for linha in linhas:
			print linha
			
	def mostrarPossibilidadesColuna(self, tabuleiro = TabuleiroCasaUnica()):
		print ('\n')
		colunas = tabuleiro.getPossibilidadesColuna()
		for coluna in colunas:
			print coluna
			
	def mostrarPossibilidadesSubtabela(self, tabuleiro = TabuleiroCasaUnica()):
		print ('\n')
		subtabelas = tabuleiro.getPossibilidadesSubtabela()
		for subtabela in subtabelas:
			print subtabela
