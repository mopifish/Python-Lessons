""" 9. EXERCISE - Looping and Input!

	You and your friends at the Cornelius Philip's Factory for Boys have recently 
	found yourselves with a lot of free-time due to supply chain issues.
	One of your favorite games you've been playing to pass the time has been the
	hit guessing game, "Bulls and Cows".

	In Bulls and Cows, two players write down a secret 4 digit number on a 
	piece of paper. Both players then try to guess the other players 
	number. If a player guessed a right digit in the right spot, they 
	receive a "bull". If they guessed a right digit but in an incorrect
	spot, they receive a "cow".

	Example:
	Secret number: 1234
	Guess: 4856
	Response: "1 cow, 0 Bulls"

	since 4 was a correct digit, but in the wrong spot, the player receives
	1 cow

	Guess 2: "1524"
	response: "1 cow, 2 bulls"

	1 and 4 are both right digits, and in the right spot, so thats 2 bulls.
	2 is right, but in the wrong spot, so thats a cow.

	The game continues on like this until one of the players win.


	Ever since picking this game up with friends though, you've discovered you're 
	ATTROCIOUS at it, and you lose every time. In orer to give yourself some sort 
	of edge, you've decided to write a simple Bulls and Cows program that will allow
	you to train by playing the game all by yourself!

	Task: Using what we've learned in our previous lessons, write a program
	that allows the user to play cows and bulls.
"""

import random

# Generate a random 4 digit number
secret_number = random.randint(1111, 9999)


