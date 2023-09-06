# -*- coding: UTF-8 -*-


class Rover(object):
	"""Classe que define o objeto Rover, o carrinho que vai explorar marte."""
	def __init__(self, rover_id="", posicao=None, direcao="", instrucoes=None):
		self.__rover_id = rover_id
		self.__posicao = posicao
		self.__direcao = direcao
		self.__instrucoes = instrucoes


	# "Getter" e "Setter" da posicao que o rover se encontra.
	@property
	def posicao(self):
		return self.__posicao

	@posicao.setter
	def posicao(self,nova_pos):
		self.__posicao = nova_pos


	# "Getter" e "Setter" da direção/direcao em que o rover está apontando
	@property
	def direcao(self):
		return self.__direcao

	@direcao.setter
	def direcao(self,nova_dir):
		self.__direcao = nova_dir

	# "Getter" e "Setter" do ID do rover
	@property
	def rover_id(self):
		return self.__rover_id

	@rover_id.setter
	def rover_id(self,nova_id):
		self.__rover_id = nova_id

	# "Getter" e "Setter" das Instruções passadar para esse rover
	@property
	def instrucoes(self):
		return self.__instrucoes

	@instrucoes.setter
	def instrucoes(self, novas_instrucoes):
		self.__instrucoes  = novas_instrucoes		

	def mover_rover(self,direcao):
		"""Método responsável por movimentar o rover """
		if direcao == 'N':
			self.posicao[0] += 0
			self.posicao[1] += 1
		elif direcao == 'S':
			self.posicao[0] += 0
			self.posicao[1] += -1
		elif direcao == 'E':
			self.posicao[0] += 1
			self.posicao[1] += 0
		elif direcao == 'W':
			self.posicao[0] += -1
			self.posicao[1] += 0
		else:
			raise Exception("Houve uma, favor verificar se as orientações do rover correspondem a uma dessas: 'N','S','E','W'.")


	def girar_rover(self,direcao,rotacao):
		""" Método resposável por girar o rover no próprio eixo"""
		if direcao == 'N': 
			if rotacao == 'L':
				self.__direcao = 'W'
			elif rotacao == 'R':
				self.__direcao = 'E'
			else:
				raise Exception("Houve uma, rotação passada é diferente de 'L' ou 'R', favor revisar o arquivo de input")
		elif direcao == 'S':
			if rotacao == 'L':
				self.__direcao = 'E'
			elif rotacao == 'R':
				self.__direcao = 'W'
			else:
				raise Exception("Houve uma, rotação passada é diferente de 'L' ou 'R', favor revisar o arquivo de input")

		elif direcao == 'E':
			if rotacao == 'L':
				self.__direcao = 'N'
			elif rotacao == 'R':
				self.__direcao = 'S'
			else:
				raise Exception("Houve uma, rotação passada é diferente de 'L' ou 'R', favor revisar o arquivo de input")
		elif direcao == 'W':
			if rotacao == 'L':
				self.__direcao = 'S'
			elif rotacao == 'R':
				self.__direcao = 'N'
			else:
				raise Exception("Houve uma, rotação passada é diferente de 'L' ou 'R', favor revisar o arquivo de input")
		else:
			raise Exception("Houve uma, existe uma orientação diferente de 'N','S','E','W', favor revisar o arquivo de input.")


	def verifica_posicao(self,posicao,instrucoes):
		if (posicao[0] < 0 or posicao[1] < 0): 
			raise ValueError("Oops, quase que um rover cai do platô, paramos o programa para que isso não acontecesse.. Por favor, revise a instrucao: %s" % instrucoes)
		else:
			return posicao

# if __name__ == '__main__':
# 	rov = Rover([0,1],"N",1,['M','L','M'])
# 	print rov.posicao
# 	print rov.direcao
# 	print "alterando\n--------\n"

# 	mover_rover
# 	print "Done\n--------\n"
# 	print rov.posicao
# 	print rov.direcao
