#9.5

class User():
	"""Tworzy użytkownika."""
	
	
	def __init__(self, first_name, last_name, city, country, login_attempts):
		"""Inicjalizacja atrybutów."""
		self.first_name = first_name
		self.last_name = last_name
		self.city = city
		self.country = country
		self.login_attempts = 10
		
	def describe_user(self):
		"""Opisuje użytkowika."""
		print("\nDane o użytkowniku: ")
		print("- Imię: " + self.first_name.title())
		print("- Nazwisko: " + self.last_name.title())
		print("- Miasto: " + self.city.title())
		print("- Kraj: " + self.country.title())
		print("- Próby logowania:" + " " + str(self.login_attempts))
		
	def greet_user(self):
		"""Wyświetla spersonalizowane powitanie."""
		print("\nWitaj " + self.first_name.title() + " " +
		self.last_name.title() + "!")
			
	def increment_login_attempts(self):
		"""Inkrementuje wartość login_attempts o 1."""
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		"""Zeruje lizcbę login_attempts."""
		self.login_attempts = 0
		
		
user_0 = User('Damian', 'Osiecki', 'Bydgoszcz', 'Polska', 1)
user_0.describe_user()
user_0.greet_user()
		
user_0.increment_login_attempts()
print("Próby logowania: ")
print(user_0.login_attempts)
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.reset_login_attempts()
print(user_0.login_attempts)
