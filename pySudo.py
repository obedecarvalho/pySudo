#!/usr/bin/python2
# -*- coding: utf-8 -*-
		
import sys
from tabuleiro import Tabuleiro
from tabuleiroCasaUnica import TabuleiroCasaUnica
from entradaSaida import SudokuBD
from simulador import Simulador

if __name__ == '__main__':
	'''
	dados = SudokuBD('teste/entrada.txt', 'teste/saida.txt')
	jogo = dados.proximo()
	while jogo:
		#tabuleiro = Tabuleiro()
		tabuleiro = TabuleiroCasaUnica()
		tabuleiro.setTabela(jogo[1:82])
		simulador = Simulador()
		dados.salvar(simulador.run(tabuleiro))
		jogo = dados.proximo()
	dados.fechar()
	'''
	jogo = '070000810000318902281470005400060000690103027000090006900054681106982000057000040'
	tabuleiro = TabuleiroCasaUnica()
	tabuleiro.setTabela(jogo)
	simulador = Simulador()
	simulador.run4(tabuleiro)
	#'''
