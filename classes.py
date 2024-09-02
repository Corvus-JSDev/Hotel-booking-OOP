from pprint import pp
import pandas as pd
import random

class User:
	pass


class Hotel:
	def __init__(self, customer_name="Customer"):
		df = pd.read_csv("hotel_data.csv")

		self.df = df
		self.customer_name = customer_name.lower()


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
	def __init__(self, hotel_id, customer_name):
		df = pd.read_csv("hotel_data.csv")

		self.hotel_id = hotel_id
		self.customer_name = customer_name.lower()
		self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()


	def generate_invoice(self):
		booking_id = random.randint(1000, 9999)
		content = f"""
		Thank you for booking with us!

		Here is your booking information:
		Booking ID: {booking_id:04}
		{self.customer_name.capitalize()}, has booked a room at \'{self.name}\'"""
		return content


if __name__ == "__main__":
	# customer_name = input("What is your name: ")
	hotel = Hotel()
	hotel.list_hotels()

	hotel_id = int(input("\nEnter the ID of the hotel: "))

	# Booking a room
	if hotel.is_available(hotel_id):
		hotel.book_room(hotel_id)

		res = Reservation(hotel_id, "Giovanni")
		print(res.generate_invoice())

	else:
		print("This hotel is unavailable")
