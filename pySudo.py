#!/usr/bin/python2
# -*- coding: utf-8 -*-
		
import sys
from tabuleiro import Tabuleiro
from tabuleiroCasaUnica import TabuleiroCasaUnica
from entradaSaida import SudokuBD
from simulador import Simulador

if __name__ == '__main__':
	#'''
	dados = SudokuBD('teste/entrada.txt', 'teste/saida.txt')
	jogo = dados.proximo()
	while jogo:
		#tabuleiro = Tabuleiro()
		tabuleiro = TabuleiroCasaUnica()
		tabuleiro.setTabela(jogo[1:82])
		simulador = Simulador()
		tabuleiro2 = TabuleiroCasaUnica()
		tabuleiro2.setTabela(simulador.run5(tabuleiro))
		dados.salvar(simulador.run(tabuleiro2))
		jogo = dados.proximo()
	dados.fechar()
	'''
	jogo = 	'060091080'\
			'109680405'\
			'050040106'\
			'600000200'\
			'023904710'\
			'004000003'\
			'907020030'\
			'305079602'\
			'040150070'
	tabuleiro = TabuleiroCasaUnica()
	tabuleiro.setTabela(jogo)
	simulador = Simulador()
	simulador.run5(tabuleiro)
	'''
