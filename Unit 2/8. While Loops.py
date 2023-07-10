""" 8. While Loops

	Q's: 
		What are while loops?
		Why are while loops useful?
		How are they different from for loops?
		
"""
""" QUICK REFERENCE 

	while(bool):
		print("Hello")

	while(True):
		break

"""

# The second type of loops we'll be focusing on is while Loops!
# While loops are essentially more primitive for loops
# But this makes them extremely powerful, because they allow you to loop
# until any boolean condition is met!

# You can loop until a number is reached, like for loops

print("Test 1: Loop while i < 10")
i = 0
while (i<10):
	print(i)
	i += 1

# Or you coul loop until the user inputs a specific word
print("Test 2: Loop until quit")
user_input = input("Type 'quit' to quit: ")
while(input != "quit"):
	user_input = input("Type 'quit' to quit: ")

# You can loop till any condition your heart desires!


# Another useful feature of while loops is the "break" statement
# This allows you to exit a loop at any point

# Break statements can be used with While True loops 
# (loops that go indefinitely), to make more flexibile loops
print("Test 3: Break upon quit")
while (True):
	user_input = input("Input [i] or [j]. [q] to quit")
	if user_input == "i":
		print("You typed i")
	elif user_input == "j":
		print("You typed j")
	elif user_input == "q":
		break;
	else:
		print("Please type i, j, or q only!")

# Or they can be used to break out of a loop early
print("\nTest 4: Early exit")
i = 0
while (i < 10):
	# We dont want negative numbers :(
	# So quit!
	if i < 0:
		break;

	i += int(input("Please type a number"))


""" YOU TRY IT!
Write a while loop that gets user input, and loops until the user types
'exit'
"""
print("\nYou Try It!:")
# Your code here....
