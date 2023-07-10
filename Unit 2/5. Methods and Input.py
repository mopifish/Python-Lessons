""" 5. String Methods and Input

	Q's: 
		If you could invent any string method, what would it  be? Why?
		
"""

# Looking through that list of methods before,
# I'm sure you thought it was cool but found 
# most of them to not have much use. 

# Where string methods really shine though 
# is interpreting user input!
# When relying on input given by a user, you
# never know what you're going to get. 
# These methods allow you to even the playing field

# By now I'm sure you're familiar with the input() function
user_input = input("> ")
# Which gets a string from the user

# Now what if you wanted to use that string in a menu?
if user_input == "blue":
	print("You picked blue")
elif user_input == "red":
	print("You picked red")

# This menu is simple enough, but it has issues. What if the user typed
# "Blue", "BLUE", "blue ", or " blue"?
# The menu would   completely break down!
# you could try this...

if user_input == "blue" or user_input == "Blue" or user_input == " Blue": #... and so on
	print("You picked blue")

# but using string methods makes this way easier!
# Try this!
user_input = user_input.lower().strip()

# Now we know for sure we have a lowercase word with no extra white space!
if user_input == "blue":
	print("You picked blue")
elif user_input == "red":
	print("You picked red")