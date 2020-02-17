#9.10

class Restaurant():
	"""Tworzy restauracje."""
	
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Inicjalizacja atrybutów."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		"""Opisuje restauracje."""
		print("Nazwa restauracji to: " + self.restaurant_name.title() + 
		". A jej kuchnia to kuchnia " + self.cuisine_type + ".")
	
	
	def open_restaurant(self):
		"""Opisuje gdziny otwarcia restauracji."""
		print("Restauracja jest otwarta 24H!")
