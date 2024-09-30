# Final Project - Tip Calculator
'''
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
Each person should pay: 

# 12% = 12 / 100 = 0.12

a = (150 * 0.12 + 150)
b = (150 * 1.12) / 5 # this is the shortcut for the above 

------------
1. Task 

We're going to build a tip calculator.
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay:
(150.00 / 5) * 1.12 = 33.6

After formatting the result to 2 decimal places = 33.60

https://appbrewery.github.io/python-day2-demo/

Very Optional Reading: Floating Point Arithmetic
https://docs.python.org/3/tutorial/floatingpoint.html


'''
# Answer

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))



tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${bill_per_person}")


'''
Alternatives
1.) 
a = tip /100
a += 1

# b = round(((bill * a) / people), 2) - cam also use this if you want to do 1 liner
b = ((bill * a) / people)
c = round(b, 2)
print(f"Each person should pay: ${c}")


2.)
a = bill * (1 + tip / 100)
b = a / people

c = round(b, 2)
print(f"Each person should pay: ${c}")

3.)
a = tip / 100 * bill + bill
b = a / people

c = round(b, 2)
print(f"Each person should pay: ${c}")


# Below is the alternative for round to 2 for 1 liner together with the print output
# print(f"Each person should pay: ${b:.2f}") 
 
'''





