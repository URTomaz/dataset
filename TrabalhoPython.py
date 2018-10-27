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