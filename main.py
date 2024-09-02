from classes import *
import pandas as pd
from pprint import pp

hotel_data = pd.read_csv("hotel_data.csv")

help_commands = """
list - Show a list of all hotels.
quit - End the program."""

# print("Welcome to hotel booking!\n")

# Booking a room
hotel = Hotel(hotel_data)
"""
if hotel.is_available():
	hotel.book_room("Gio")

	res = Reservation("hotel_test", "Giovanni")
	print(res.generate_invoice())

else:
	print("This hotel is unavailable")
"""




while True:
	user_choice = input("\nWhat would you like to do: ").lower().strip()


	match user_choice:
		case "l" | "list":
			print(" ")
			print(hotel_data)

		case "h" | "help":
			print(help_commands)

		case "q" | "quit":
			print("\nEnding program, goodbye.")
			break

		case _:
			print(f"`{user_choice}` is not a valid command. Type `help` for a list of commands.")

