# Variables


'''
Sample:

name = "Jack"
print(name)

name = "Elizar"
print(name)

'''

'''
Task **

Learn to store values in containers for later use. Variables is a concept in programming that allows us to give a label to a piece of data so that we can refer or reference that data using the chosen variable name. We will see in this lesson how to create variables and how to use the variables to access the contained value.

PAUSE 1. Check the length of the user input
Using what you have learnt about the len() function and the input() function. Try to print out the number of characters in the user input. Write everything in just 1 line of code.

'''

# Answer 1
print(len(input("What is your name?")))

'''
PAUSE 2. Split everything into variables.
Split each step in the previous exercise into a separate variable. One variable called username and one called length. Use the variable username in the len calculation.

'''

# Answer 2

username = input("What is your name?")
length = len(username)

print(length)


'''
Task 3
We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.

'''

# Answer

glass1 = "milk"
glass2 = "juice"


a = glass1
glass1 = glass2
glass2 = a