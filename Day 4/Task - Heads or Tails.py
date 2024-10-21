''' Activity
# PAUSE 1 - Heads or Tails
# Create a coin flip program using what you have learnt about randomisation in Python. It should randomly print "Heads" or "Tails" everytime it is run.

# Hint 
You'll need to think about what you have learnt about conditional statements in Python.

'''

# Answer 1
import random

# Generate a random number between 0 and 1
random_number = random.randint(0, 1)
# If the random number is less than 0.5, print "Heads"
if random_number == 0:
    print("Heads")
    # If the random number is 1 "Tails"
else:
    print("Tails")
print(f"The random number is {random_number}")






# My Answer 2
''' 
import random

# Generate a random number between 0 and 10
random_number = random.randint(1, 10)
# If the random number is less than 5, print "Heads"
if random_number <= 5:
    print("Heads")
    # If the random number is not less than 5, print "Tails"
else:
    print("Tails")
print(f"The random number is {random_number}")


'''