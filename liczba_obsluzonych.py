#9.4

class Restaurant():
	"""Tworzy restauracje."""
	
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Inicjalizacja atrybutów."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0


	def describe_restaurant(self):
		"""Opisuje restauracje."""
		print("Nazwa restauracji to: " + self.restaurant_name.title() + 
		". A jej kuchnia to kuchnia " + self.cuisine_type + ". " +
		"Restauracja obsłużyła: " + str(self.number_served) + " gości.")
	
	
	def open_restaurant(self, time_open):
		"""Opisuje gdziny otwarcia restauracji."""
		print("Restauracja jest otwarta " + str(time_open) + "H!")
		
		
	def set_number_served(self, number_served):
		"""Pozwala na zdefiniowanie liczby obsłużonych klientów."""
		self.number_served = number_served
		
	def increment_number_served(self, increment_number_served):
		"""Pozwala na inkrementacje liczby obsłużonych klientów."""
		self.number_served += increment_number_served

restauracja_0 = Restaurant('Chińczyk', 'Chińska')
restauracja_0.describe_restaurant()
restauracja_0.open_restaurant(24)
print("\n")

restauracja_0.number_served = 10
restauracja_0.describe_restaurant()

print("\n")
restauracja_0.set_number_served(200)
restauracja_0.describe_restaurant()

print("\n")
restauracja_0.increment_number_served(50)
restauracja_0.describe_restaurant()
