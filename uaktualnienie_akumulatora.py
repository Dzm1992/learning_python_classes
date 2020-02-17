#9.9

class Car():
	"""Prosta próba zaprezentowania samochodu."""
	
	
	def __init__(self, make, model,  year):
		self.make = make
		self.model = model
		self.year = year
		
		
class EletricCar(Car):
	"""Przedstawia cechy charakterystyczne samochodu elektrycznego."""
	def __init__(self, make, model, year):
		"""Inicjalizacja atrybutów klasy nadrzędnej."""
		super().__init__(make, model, year)	
		self.battery = Battery()
		
class Battery():
	"""Prosta próba modelowania akumulatora samochodu elektrycznego."""
	def __init__(self, battery_size=70):
		"""Inicjalizacja atrybutów akumulatora."""
		self.battery_size = battery_size
		
	def upgrade_battery(self):
		"""Aktualizuje wielkość akumulatora."""
		if self.battery_size != 85:
			self.battery_size = 85
		else:
			self.battery_size = self.battery_size


car_0 = EletricCar('Tesla', 'Model S', '2016')
print("Aktualna pojemność akumulatora to " + str(car_0.battery.battery_size) + "!")
car_0.battery.upgrade_battery()
print("Aktualna pojemność akumulatora to " + str(car_0.battery.battery_size) + "!")
	
	
