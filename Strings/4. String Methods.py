""" 4. String Methods

	Q's: 
		What are string methods?
		Why are they useful?
		Which of these methods do you think would be the most useful? Why?
"""

# String methods are methods you can use to modify strings.
	# Side Q: What is a method?
	# A method is just a function that belongs to an object. 
	# All of the following are functions that BELONG to string objects
	# As a result, they're called methods

# String methods can be used like this: 
# string_name.method_name()

str_one = "Hello"


print("-- Upper Method --")
print(str_one.upper())

# String one was the string variable, and upper was the method name
# So typing "str_one.upper()" makes str_one upper case!
# The '.' is very important, as it tells python that the following 
# function BELONGS to the string

# You can also do this without variables

print("Hello".upper())
print()

# Here are some other useful string methods:

""" .lower() """
	# Returns a lowercase version of the string
print("-- Lower Method --")
print("HELLO")
print("HELLO".lower())
print()

""" .strip() """
	# Removes excess white space at the beginning and end of strings
print("-- Strip Method --")
print("   Hello!   ")
print("   Hello!   ".strip())
print()

""" .replace(a, b) """
	# Replaces any part of a string with a different string
print("-- Replace Method --")
print("Hullo!")
print("Hullo!".replace("Hu", "He"))
print()

""" .split(a) """
	# Splits a string into a list based on the given delimeter (a)
print("-- Split Method --")
print("One, Two, Three")
print("One, Two, Three".split(", "))
print()

# This is only a few of pythons MANY string methods
# The amount of string methods is one thing that makes python
# So useful and quick to code in!
# If you'd like to see more, go here:
# https://www.w3schools.com/python/python_ref_string.asp