# Modulo - %
# // and / gives you the float or whole output
# %,  Gives you only the remainder of a division
# We are going to check for the Age


'''

The modulo operator gives you the remainder of a division.

6 % 2 #will be 0

6 % 5 #will be 1

6 % 4 #will be 2

PAUSE 1 - What is 10 % 3?
What do you think this will output?

print(10 % 3)

PAUSE 2 - Check Odd or Even
Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".


'''

# Answer 1
print(10 % 3) # Answer is 1




# Answer 2
number_to_check = int(input("Enter a number:\n"))
temp = number_to_check

if number_to_check % 2 == 0:

    print(f"Provided number {temp} is Even")
else:
    print(f"Provided number {temp} is Odd")