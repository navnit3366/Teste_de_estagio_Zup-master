#-*- coding: UTF-8 -*-

from rover import *


def imprime_boas_vindas(nome):
	print "\n\t===== Simulação Rovers da NASA =====\n"
	print " Bem Vindo %s! Leia as instruções atentamente.\n" % nome
	print " **Instruções:**\n 1-Crie um arquivo com os dados de entrada;"
	print "  Os dados são: Primeira Linha: Localização do Platô (Ex: 5 5)"
	print "  Segunda Linha: Localização e direção que o Rover aponta (Ex: 1 2 N)"
	print "  Terceira Linha: Movimentações do Rover (Ex: MMLRMLRM)\n\n"
	print "  **Informação Importante:** Direções válidas:['N','S','E','W'], significando respectivamente: Norte,Sul,Leste,Oeste."
	print "  **Informação Importante:** Movientações válidas:['M','L','R'], significando respectivamente: mover para frente,girar em seu eixo para esquerda,girar para direita"
	print " Para sair a qualquer hora  do programa basta apertar ctrl+c"
	print "\nNo final do programa será gerado um arquivo(resultado.txt) com o resultado da simulação!\n"
	
	print "\tBom Teste!"
	print "\t==========\n"


def abre_arquivo():
	arquivo = raw_input("Entre com o (caminho e) nome do arquivo: ")
	try:
		with open(arquivo, "r") as texto:
			informacoes_do_arquivo = texto.read().splitlines()
			print "\nArquivo lido, aguarde.."
		return informacoes_do_arquivo
	except (TypeError,IOError) as error:
		print "\n** Houve um erro na hora de abrir o arquivo: %s **\n" % error
	

def itera_arquivo(l):
	while l:
		yield l[0:2]
		del l[0:2]	

def valida_tamanho_plato(coordenada_max_plato):
	coordenada_max_plato[0] = int(coordenada_max_plato[0])
	coordenada_max_plato[1] = int(coordenada_max_plato[1])
	if coordenada_max_plato[0] <= 0 and coordenada_max_plato[1] <= 0:
		raise Exception("\n **Coordenadas do Platô não são válidas, elas devem ser no mínimo maior que 0**\n")


class InicializadorDeRovers(object):
	"""Método responsável por fazer análise do arquivo e validar ou não os inputs"""
	def __init__(self):
		self.rovers = []

	def pega_dados_do_input(self, arquivo):
		"""Método responsável por ler os dados do arquivo e criar os rovers"""
		for id_sequencial, lista_com_inputs in enumerate(itera_arquivo(arquivo)):

			rover = Rover()
			rover.rover_id = id_sequencial
			segunda_linha = lista_com_inputs[0].split(" ")
			rover.posicao =  list(int(valor) for valor in segunda_linha[0:2])
			rover.direcao = segunda_linha[-1]
			terceira_linha = lista_com_inputs[1]
			rover.instrucoes = (terceira_linha)

			self.rovers.append(rover)

	def inicia_rovers(self):
		"""Método responsável por fazer os lançamentos dos rovers e o output"""
		posicao_final = " "
		try:
			with open("resultado.txt", 'w') as resultado:
				for rov in self.rovers:
				 	for movimento in rov.instrucoes:
				 		rov.verifica_posicao(rov.posicao[:2],rov.instrucoes)
				 		if movimento == 'M':
				 			rov.mover_rover(rov.direcao)
				 		else:
				 			rov.girar_rover(rov.direcao,movimento)
				 		saida_final = posicao_final.join(str(valor) for valor in rov.posicao[:2])+ " " + rov.direcao
					resultado.write(saida_final+'\n')
			print "=========================================================================="
			print "Acabamos por aqui.. Por Favor, confira o arquivo 'resultado.txt'. Obrigado\n"
			print "=========================================================================="
		except (TypeError,IOError) as error:
			print "\n** Houve um erro na hora de abrir o arquivo: %s **" % error



if __name__ == '__main__':
	nome = raw_input("Qual seu nome? ")
	imprime_boas_vindas(nome)

	arquivo = abre_arquivo()
	try:
		tamanho_max_do_plato = arquivo.pop(0)
		tamanho_max_do_plato = tamanho_max_do_plato.split()

		tamanho_max_do_plato[0] = int(tamanho_max_do_plato[0])
		tamanho_max_do_plato[1] = int(tamanho_max_do_plato[1])

		valida_tamanho_plato(tamanho_max_do_plato)

		inicia = InicializadorDeRovers()
		print "\n....\n"
		inicia.pega_dados_do_input(arquivo)
		inicia.inicia_rovers()
	except (AttributeError, TypeError, IOError, UnboundLocalError) as error:
		print "\n** Oops.. Algo aconteceu durante a execução do programa, confirme se você informou tudo corretamente. %s **\n" % error
