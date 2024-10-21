# Random Module 2

#  Pseudo Random Number - Python uses is something called the Mersenne Twister -  [Link: https://en.wikipedia.org/wiki/Mersenne_Twister ]
# Discusses about Psuedo Random Numbers: https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
# Functions that will allow you generate random Integer / Whole / Floating numbers - https://docs.python.org/3/library/random.html


# 1. Random Integers
import random

random_integer = random.randint(1,10) # random.randint(a:1, b:10)
print(random_integer)


# But how can we create our own modules, and how do modules work anyways?
''' 
1. Create a new file and name it - ex: my_module.py
2. Add variables and others in it. or functions > Save
3. Go to the target page or file you like to use it.
4. Import the module using - import my_module
'''


import my_module
print(my_module.my_favourite_number) # my_favourite_number is a variable in my_module.py

# 2. Random Floating Point Numbers
# a. No whole number
random_number_0_to_1 = random.random() * 10 # random.random() is float and multiplied to 10
print(random_number_0_to_1)


# b. With whole number
random_float = random.uniform(1, 10)
print(random_float)

''' Activity
# PAUSE 1 - Heads or Tails
# Create a coin flip program using what you have learnt about randomisation in Python. It should randomly print "Heads" or "Tails" everytime it is run.

# Hint 
You'll need to think about what you have learnt about conditional statements in Python.

'''

