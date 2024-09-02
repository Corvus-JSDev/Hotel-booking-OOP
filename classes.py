from pprint import pp
import pandas as pd

class User:
	pass


class Hotel:
	def __init__(self, customer_name="Customer"):
		self.customer_name = customer_name.lower()
		self.df = pd.read_csv("hotel_data.csv")


	def book_room(self, hotel_id):
		# Reassign the value to "no" to show it has been booked an is full
		df = self.df
		df.loc[df["id"] == hotel_id, "available"] = "no"

		# Save the changes
		df.to_csv("hotel_data.csv", index=False)  # Set index=False so python doesn't add another index

		print("Your room has been booked")


	def list_hotels(self):
		pp(self.df)


	def is_available(self, hotel_id):
		try:
			df = self.df
			row = df.loc[df["id"] == hotel_id]
			available = row["available"].squeeze()

			return True if available == "yes" else False
		except ValueError:
			return False


class Reservation:
	def __init__(self, hotel_obj, customer_name):
		self.hotel_obj = hotel_obj.lower()
		self.customer_name = customer_name.lower()


	def generate_invoice(self):
		content = f"{self.customer_name} has booked a room at {self.hotel_obj}"
		return content


if __name__ == "__main__":
	hotel = Hotel("Gio")
	hotel.list_hotels()

	hotel_id = int(input("\nEnter the ID of the hotel: "))

	# Booking a room
	if hotel.is_available(hotel_id):
		hotel.book_room(hotel_id)

		"""
		res = Reservation("hotel_test", "Giovanni")
		print(res.generate_invoice())
		"""

	else:
		print("This hotel is unavailable")
