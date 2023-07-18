""" 11. Logic and Problem Solving

	Q's: 
		What are some other problems you can solve with these methods?
		Does this only work for programming?
		
"""
""" QUICK REFERENCE 
	
	P - Identify the problem
		- Divide the problem
		- Turn it into logical statements
	T - Identify your Tools
	B - Brainstorm ways you might use your tools to solve the problem
	S - Use your tools to Solve the Problem
	
"""

# When you look at any problem, especially complex programming problems
# It can very easily overwhelm you and lead to a lot of confusion

# Because of this, it's important to use problem solving strategies to
# break down a problem into bite sized chunks!

""" P - Identify the problem

Identifying the problem is essentially what we did in the last lesson
By turning a problem into a logical statement, we turn it into a 
format that is both easily understood, and easy to turn into code.

sometimes a problem seems to big and too complex to break up into 
statements though...

When this happens, try Dividing the problem. 
Take the current task, and break it up into two different things
you need to do to achieve that task. Continue doing this until
you have something you can do Right Now

For example!

- Write a program that plays a game of black jack

  - Tasks:

  	- Research the rules of blackjack
  	- Program blackjack
		- Program a deck of cards
		- Program a turn structure
			- Get user input
			- Compare user input to choose action
				- Program each action
					- Program draw card
					- Program flip hand
				- Program the if statement

				... And so on!!

By the time you finish, you'll have a step by step list
of little micro-problems you need to solve!

You can then use your logic skills to turn each micro problem into
a logical statement. Once you've done that, you've pretty much written
the entire program without every writing a single
line of code!

"""

""" T - Identify your tools

Okay so we have a bunch of logical statements... now what?
In programming you, your goal is to translate a logical solution
into code.

We can use woodworking as an analogy for this! In woodworking,
your goal is to translate an idea into a wooden creation.

In order to do this, you're going to need a toolbelt. Before you 
even begin a project, you're going to think about what tools 
and materials  you're going to use to assemble it.

What type of wood will you use? (Which programming language)
Will you use a hammer and nails, or screws? (If statements or switch statements)
What about stain and finish? (Code style)
What kind of joint will you use to assemble it? (What data structures will you use?)

Before you solve ANY problem, always try to assemble your toolbelt first! 
You can always switch out tools, or never use some, but it helps to have 
an idea of what you're going to use  to solve this problem.


Now, lets take the sheep counting probelm from last lesson as an example.
Whenever I encounter a logical statement,or micro-problem, 
that I need to translate, the first thing I'm gonna do
is think about what tools I'm going to use to translate it. 

For example:
"
If there is a next value, try premise Q, and then go to the next value
there is a next value
Try premise Q, then go to the next value
"

I know we're provided a list filled with boolean statements, so thats
two tools already given to me. 
Given the nature of the statement, I also know I want to go through
every item IN the list. If I couldn't think of a way to do this in 
code, I would at this point google it and find a way. But, since
I've been doing this for so long, I know I want to use a 
"for-each loop". Finally, premise Q sounds a LOT like a function doesn't
it? So I'll use functions as well.

So in review, I have a problem:
- Go through every item in a list
and a toolbelt:
- List
- Boolean statements
- For each loops
- Functions

I've practically turned this complex problem into a jigsaw puzzle!
I have all the pieces, now I just have to think of ways to assemble them
into my desired shape.

YOU TRY IT!
 Go back to the previous lesson, and try assembling "tool belts"
 for each of the problems you broke down.
"""