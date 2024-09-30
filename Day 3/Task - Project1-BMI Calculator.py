# Project 1 - BMI Calculator

'''
BMI Calculator with Interpretations
# BMI - Body Mass Index

Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

If the bmi is under 18.5 (not including), print out "underweight"

If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

If the bmi is 25 (including) or over, print out "overweight"

Refer to this graphic for help:

# See Project 1 pic

'''

# Answer 1 - provided by Udemy

weight = 85
height = 1.85
 
bmi = weight / (height ** 2)
 
if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")



'''

# Answer 2 - This is correct - this is my 1st entry adding input for confirmation
a = float(input(f"Enter BMI:\n"))


if a < 18.5:
    print("Underweight")
elif a == 18.5:
    print("Normal weight")
elif a < 25:
    print("Normal weight")    
else:
    print("Overweight")



# Answer 3 - Entry from Chatgpt
bmi = float(input(f"Enter BMI:\n"))
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("Overweight")


'''

