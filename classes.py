class User:
	pass


class Hotel:
	def __init__(self, hotel_data, hotel_id=134):
		self.hotel_data = hotel_data
		self.hotel_id = hotel_id


	def book_room(self, name_of_user):
		pass


	def list_hotels(self):
		pass


	def is_available(self):
		print(self.hotel_data[self.hotel_id])


class Reservation:
	def __init__(self, hotel_obj, customer_name):
		self.hotel_obj = hotel_obj.lower()
		self.customer_name = customer_name.lower()


	def generate_invoice(self):
		content = f"{self.customer_name} has booked a room at {self.hotel_obj}"
		return content
