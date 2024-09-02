from classes import *
import pandas as pd
from pprint import pp

help_commands = """
list - Show a list of all hotels.
quit - End the program."""

print("Welcome to hotel booking!\n")

while True:
	# user_choice = input("\nWhat would you like to do: ").lower().strip()
	user_choice = "q"

	match user_choice:
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

