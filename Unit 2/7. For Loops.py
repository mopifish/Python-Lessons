""" 7. For Loops

	Q's: 
		What are for loops?
		Why are for loops useful?
		
"""
""" QUICK REFERENCE 

for i in range(start, end, count_by):
	print()

e.g.:
	for i in range(0, 10, 2):
		print(i)

output: 
	0, 2, 4, 6, 8

"""

# Loops are ways to execute a piece of code as many times as you want

# There are two types of loops, and the first one we'll be looking at is the
# FOR LOOP

# For loops allow you to loop for a SET NUMBER of times
# The following code loops 10 times


print("Test 1")
for i in range(10):
	print("Hello")

# The i in a for loop represents the current position in the loop
# The above for loop is basically going
# "i = 0. While i is less than 10, add 1 to i"
# Which leads to it printing out the following...
print("\nTest 2: Count up to 10")
for i in range(10):
	print(i)

# ---- Bonus Features -----
# In the previous examples, we used the expression "for i in range(10)"
# to count from 0 up to 10. 
# Since we only put in 1 number (10), python automatically assumed the starting position was 0
# But what if we want to start at 1? or 2? or 3?
# We only have to add a number IN FRONT of our ending number like so:
print("\nTest 3: Start at 1")
for i in range(1, 10):
	print(i)

# We can also choose how much is added to i every loop
# by adding a number AFTER the ending number
print("\nTest 4: Count by 3's ")
for i in range(0, 10, 3):
	print(i)

# NOTE: If you add a "count-by" number, you also have to specify a start number!

""" YOU TRY IT!
Write a for loop that counts from 0 to 144, and counts by 12's
"""
print("\nYou Try It!:")
for i in range(0, 144, 12):
	print(i)