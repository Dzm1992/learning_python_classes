#9.12

from wiele_modulow_2 import User
	
class Admin(User):
	"""Tworzy admina."""
	
	def __init__(self, first_name, last_name, city, country):
		"""Inicjalizacja admina i atrybutów admina."""
		super().__init__(first_name, last_name, city, country)
		self.privileges = Privileges()
		
		
class Privileges():
	"""Przywileje."""
	
	
	def __init__(self, privileges='Admin może banować użytkowników!'):
		"""Inicjalizacja atrybutów."""
		self.privileges = privileges
		
		
	def show_privileges(self):
		"""Wyświetla informacji o przywilejach."""
		print(self.privileges)
