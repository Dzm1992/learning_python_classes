#9.6

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
		

class IceCreamStand(Restaurant):
	"""Tworzy budkę z lodami."""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""
		Inicjalizacja atrybutów klasy nadrzednej. Następnie inicjalizacja 
		atrybutów charakterystycznych dla budki z lodami.
		"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = 'Jagodowe'
		
	def ice_creams(self):
		print("Dostępne lody, to Lody: " + self.flavors + "!")
		
Budka_lody = IceCreamStand('Super Lody', 'Lodziarnia')
Budka_lody.describe_restaurant()
print(Budka_lody.flavors)
Budka_lody.ice_creams()
