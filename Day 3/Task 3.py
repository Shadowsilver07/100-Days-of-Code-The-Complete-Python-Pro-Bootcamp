# Nested if statements and elif statements

'''
Syntax
if condition1:
    if another condition:  # This is the nested if up until to its else
      do this # both if needs to be true 
    else:
      do this # the 1st if needs to be true and the next is false
else:
  do this # 1st if needs to be false

  

You can put if/else statements inside other if/else statements. This is known as nesting. e.g.

if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
if english_score >= 90:
    print("You're good at english)
In this case only when a student has over 90 on maths and english, do they get "You are good at everything".

Note: You can also have if statements that don't have a paired else statement.  
'''


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")


'''
New challenge: See pic. 3.1 
< 12 "5$"
12 - 18 "$7"
> 18 "$12"


# Use - if / elif / else

if condition1: # if condition is met will bypass the elif
    do A
elif condition2: # we can add more elif until condition is met
    do B
.
.
.    
else:
    do C
'''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")


