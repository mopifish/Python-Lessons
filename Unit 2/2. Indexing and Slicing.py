""" 2. Indexing and Slicing

	Q's: 
		How are strings lists?
		What are some other ways this could be useful?
"""

# Strings are also lists!
# If you look closely, you'll notice a string is actually just a list of characters
# This means we can access them the same way we access lists
# by 'indexing

alphabet = "abcdefg"
print("The first letter of the alphabet is: " + alphabet[0])

# By using open brackets [ ] after the variable name, and inserting an index
# We can get a character at the given position
# In the above example, we got the 0'th character, or the 1st character in the string

# Aside from indexing, we can also do something called "slicing"
# Slicing is where we use an index to get multiple characters in a string

print("Do you know your " + alphabet[0:3] + "'s?" )

# By using a colon in the index, we can tell python to get every character from
# 0 to 3! In human speak, the : means "to" and the [] mean "get"
# alphabet[0:3] just means "get letters 0, 1, and 2 from alphabet!"
# Note that 3 isn't inclusive, meaning it'll get every letter UP TO 3, and not index 3 itself

# You don't always need two numbers to slice. If you leave one slot blank, the computer will fill it in for you
# With the first or last index of the string.

# Get every letter up to the 3rd letter
print("I know my " + alphabet[:3] + "'s!")
# Even though we didn't include 0, by leaving it blank the computer was able to infer

# This works in the reverse too
print("What about your " + alphabet[3:] + "'s?")

# Finally, you can also control how many characters are grabbed from a string slice
# If you add another colon, it allows you to print every x letter! 
# the following example prints every 3rd letter
print(alphabet[::3])

# Translated into english, the 2nd colon is like saying "by"
# And since the first two colons are empty, python automatically fills them in with the first and last index
# So all together it reads: "get every 3rd letter between the first and last letter of the alphabet!"

""" You try it!
Fred accidentally put too many letters into his string variable
can you use string slicing to remove the extras, and just print "banana"?

"""
# string = bananasdjkjh
# print(string)


