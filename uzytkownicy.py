#9.3

class User():
	"""Tworzy użytkownika."""
	
	
	def __init__(self, first_name, last_name, city, country):
		"""Inicjalizacja atrybutów."""
		self.first_name = first_name
		self.last_name = last_name
		self.city = city
		self.country = country
		
		
	def describe_user(self):
		"""Opisuje użytkowika."""
		print("\nDane o użytkowniku: ")
		print("- Imię: " + self.first_name.title())
		print("- Nazwisko: " + self.last_name.title())
		print("- Miasto: " + self.city.title())
		print("- Kraj: " + self.country.title())
		
		
	def greet_user(self):
		"""Wyświetla spersonalizowane powitanie."""
		print("\nWitaj " + self.first_name.title() + " " +
		self.last_name.title() + "!")
			
		

user_0 = User('Damian', 'Osiecki', 'Bydgoszcz', 'Polska')
user_0.describe_user()
user_0.greet_user()
		
user_1 = User('Przemek', 'Kowalski', 'Toruń', 'Polska')
user_1.describe_user()
user_1.greet_user()

user_2 = User('John', 'Smith', 'Manchester', 'UK')
user_2.describe_user()
user_2.greet_user()
