""" 11. Logic in Programming

	Q's: 
		Why is breaking a problem up into logical statements helpful?
		Why do logical statements look so much like code?? (Try using deductive reasoning!)
		
"""
""" QUICK REFERENCE 
	
	
"""



# Deductive reasoning is also very useful  since it's the 
# Primary form of reasoning we use in programming!

p = True

if p:
	print("q")

# If p, then q. P is true, therefore, Q!

# Whenever you want a computer to do something, 
# You have to think of the premise you give it that will
# lead it to logically deduce what you want it to deduce

# Lets try using logical deduction to solve this problem:
# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15

"""
Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.

Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue which is at the end of the array:

[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   7      6      5      4      3            2      1

If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.

Note: there will always be exactly one wolf in the array.
Examples

Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

Input: ["sheep", "sheep", "wolf"]
Output: "Pls go away and stop eating my sheep"

"""

# Ignoring python and programming entirely, lets break this problem 
# down into a logical statement.

"""
If the wolf is in front, you will tell the wolf to go away.
Otherwise, if the wolf is not in front, you will warn the sheep in front of it

The wolf is in front
You tell the wolf to go away

"""
# Now that we've broken up that problem into a simple logical statement, 
# It seems way easier to digest doesnt it? 

# In the next lesson we'll focus on where to go next, but for now
# Let's keep trying to break up these problems into logical statements

"""
https://www.codewars.com/kata/54edbc7200b811e956000556

Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined
"""

# This problem is a little bit more complex.
# Even two premises, like before, wouldn't solve it!
# So lets try Nesting two premises!

"""
If there is a next value, try premise Q, and then go to the next value
there is a next value
Try premise Q, then go to the next value


Premise Q:
If a value is true, add 1 to the sheep count
The value is true
Add 1 to sheep count

"""

# We haven't written any code, this is all instruction
# A human is perfectly capable of doing
# And yet it almost LOOKS like code doesnt it?

# This is because code is just a series of logical statements!

""" YOU TRY IT!
Translate each of the following problems into a logical statement!
"""
# https://www.codewars.com/kata/5c374b346a5d0f77af500a5a

# (this one seems hard, but only needs two statements!) https://www.codewars.com/kata/5b853229cfde412a470000d0
