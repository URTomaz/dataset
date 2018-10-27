import random
class _Node:
	def __init__(self, item):
		self.item = item
		self.proximo = None
		self.anterior = None

	def __str__(self):
		return " [" + str(self.item) + "] "

class ListaDEC:
	def __init__(self):
		self._inicio = None
		self._fim = None
		self._size = 0

	def __len__(self):
		return self._size

	def isEmpty(self):
		return self._inicio is None


	def inserirInicio(self, item):
		node = _Node(item)
		if self.isEmpty():
			self._inicio = node
			self._fim = node

		else:
			node.proximo = self._inicio
			self._inicio.anterior = node

			self._fim.proximo = node
			node.anterior = self._fim

			self._inicio = node

		self._size += 1


	def inserirFim(self, item):
		node = _Node(item)
		if self.isEmpty():
			self._inicio = node
			self._fim = node

		else:
			node.anterior = self._fim
			node.proximo = self._inicio

			self._fim.proximo = node
			self._inicio.anterior = node

			self._fim = node

		self._size += 1

	def __repr__(self):
		string = ""
		aux = self._inicio
		string += str(aux)
		while aux != self._fim:
			aux = aux.proximo
			string += str(aux)

		return string

	def travessia(self):
		print(self)


	def inserirAntes(self, item, indice):
		if not self.isEmpty() and indice <= len(self) and indice > 0:
			
			node = _Node(item)

			i = 0
			aux = self._inicio
			i += 1

			while aux != self._fim and i != indice:
				aux = aux.proximo
				i += 1

			if  aux.anterior == self._fim:
				
				node.proximo = aux
				aux.anterior.proximo = node
				node.anterior = aux.anterior
				aux.anterior = node

				self._fim = node

			else:
				node.proximo = aux
				aux.anterior.proximo = node
				node.anterior = aux.anterior
				aux.anterior = node

			self._size += 1


	def inserirDepois(self, item, indice):
		if not self.isEmpty() and indice <= len(self) and indice > 0:
			
			node = _Node(item)

			i = 0
			aux = self._inicio
			i += 1

			while aux != self._fim and i != indice:
				aux = aux.proximo
				i += 1

			if aux.proximo == self._inicio:
				
				node.anterior = aux
				aux.proximo.anterior = node
				node.proximo = aux.proximo
				aux.proximo = node

				self._inicio = node

			else:
				node.anterior = aux
				aux.proximo.anterior = node
				node.proximo = aux.proximo
				aux.proximo = node

			self._size += 1

	def removerInicio(self):
		self._fim.proximo = self._inicio.proximo
		self._inicio.proximo.anterior = self._fim
		self._inicio = self._inicio.proximo

		self._size -= 1

	def removerFim(self):
		self._inicio.anterior = self._fim.anterior
		self._fim.anterior.proximo = self._inicio
		self._fim = self._fim.anterior

		self._size -= 1

	def retornarInicio(self):
		return self._inicio

	def retornarFim(self):
		return self._fim

	def retornarAnterior(self, indice):
		if not self.isEmpty() and indice <= len(self) and indice > 0:
			
			i = 0
			aux = self._inicio
			i += 1

			while aux != self._fim and i != indice:
				aux = aux.proximo
				i += 1

			return aux.anterior

	def retornarProximo(self, indice):
		if not self.isEmpty() and indice <= len(self) and indice > 0:
			
			i = 0
			aux = self._inicio
			i += 1

			while aux != self._fim and i != indice:
				aux = aux.proximo
				i += 1

			return aux.proximo

cartas = []
cartas.append('As de copas')
cartas.append('Dois de copas')
cartas.append('Três de copas')
cartas.append('Quatro de copas')
cartas.append('Cinco de copas')
cartas.append('Seis de copas')
cartas.append('Sete de copas')
cartas.append('Oito de copas')
cartas.append('Nove de copas')
cartas.append('Dez de copas')
cartas.append('Valete de copas')
cartas.append('Rainha de copas')
cartas.append('Rei de copas')

cartas.append('As de paus')
cartas.append('Dois de paus')
cartas.append('Três de paus')
cartas.append('Quatro de paus')
cartas.append('Cinco de paus')
cartas.append('Seis de paus')
cartas.append('Sete de paus')
cartas.append('Oito de paus')
cartas.append('Nove de paus')
cartas.append('Dez de paus')
cartas.append('Valete de paus')
cartas.append('Rainha de paus')
cartas.append('Rei de paus')

cartas.append('As de ouros')
cartas.append('Dois de ouros')
cartas.append('Três de ouros')
cartas.append('Quatro de ouros')
cartas.append('Cinco de ouros')
cartas.append('Seis de ouros')
cartas.append('Sete de ouros')
cartas.append('Oito de ouros')
cartas.append('Nove de ouros')
cartas.append('Dez de ouros')
cartas.append('Valete de ouros')
cartas.append('Rainha de ouros')
cartas.append('Rei de ouros')

cartas.append('As de espadas')
cartas.append('Dois de espadas')
cartas.append('Três de espadas')
cartas.append('Quatro de espadas')
cartas.append('Cinco de espadas')
cartas.append('Seis de espadas')
cartas.append('Sete de espadas')
cartas.append('Oito de espadas')
cartas.append('Nove de espadas')
cartas.append('Dez de espadas')
cartas.append('Valete de espadas')
cartas.append('Rainha de espadas')
cartas.append('Rei de espadas')


random.shuffle(cartas)


Deck = ListaDEC()
x = 0
for carta in cartas:
    if x %2 == 0:
        Deck.inserirFim(carta)
    else:
        Deck.inserirInicio(carta)
    x+=1
print("Cartas Embaralhadas:")
Deck.travessia()
print("------------")
jogador1 = []
print("Jogador 1:")
for x in range(0, 2):
    jogador1.append(Deck.retornarFim())
    print(Deck.retornarFim())
    Deck.removerFim()
print("------------")

jogador2 = []
print("Jogador 2:")
for x in range(0, 2):
    jogador2.append(Deck.retornarInicio())
    print(Deck.retornarInicio())
    Deck.removerInicio()
print("------------")

jogador3 = []
print("Jogador 3:")
for x in range(0, 2):
    jogador1.append(Deck.retornarFim())
    print(Deck.retornarFim())
    Deck.removerFim()
print("------------")

jogador4 = []
print("Jogador 4:")
for x in range(0, 2):
    jogador2.append(Deck.retornarInicio())
    print(Deck.retornarInicio())
    Deck.removerInicio()
print("------------")

print("Mesa:")
for x in range(0, 5):
    jogador2.append(Deck.retornarInicio())
    print(Deck.retornarInicio())
    Deck.removerInicio()
print("------------")
print("Cartas Sobrando:")
Deck.travessia()

