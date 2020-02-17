#9.14
"""Generuje losowy rzut kością."""

from random import randint


class Die():
	"""Tworzy kostkę."""
	
	def __init__(self, sides=6):
		"""Inicjalizacja atrybutów."""
		self.sides = sides
		
	def roll_die(self):
		"""Rzut kostką."""
		print(randint(1, self.sides))
		
		
kostka = Die()
	
for x in range(1,11):
	print("Rzut kostką: ")
	kostka.roll_die()
	print("\n")
			

