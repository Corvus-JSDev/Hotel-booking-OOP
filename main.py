from classes import *

help_commands = """
book - Book a hotel
list - Show a list of all hotels.
quit - End the program."""

print("Welcome to hotel booking!")

while True:
	user_choice = input("\nWhat would you like to do: ").lower().strip()
	hotel = Hotel()

	match user_choice:
		case "b" | "book":
			customer_name = input("What is your name: ")

			hotel.list_hotels()

			hotel_id = int(input("\nEnter the ID of the hotel: "))

			# Booking a room
			if hotel.is_available(hotel_id):
				credit_card = SecureCreditCard(card_number="1234567890123456", exp_date="05/27",
									 holder="JOHN SMITH",
									 cvc="123")  # Skipping the user input step for simplicity

				given_pw = input("What is the password for the credit card: ")
				if credit_card.validate() and credit_card.auth(given_pw=given_pw):
					hotel.book_room(hotel_id)

					res = Reservation(hotel_id, customer_name)
					print(res.generate_invoice())
				else:
					print("Invalid Credit Card Credentials")

			else:
				print("This hotel is unavailable")


		case "l" | "list":
			print(" ")
			print(hotel.list_hotels())


		case "h" | "help":
			print(help_commands)


		case "q" | "quit":
			print("\nEnding program, goodbye.")
			break


		case _:
			print(f"`{user_choice}` is not a valid command. Type `help` for a list of commands.")

