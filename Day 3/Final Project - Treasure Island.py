# Final Project - Treasure Island

'''
# Task 

1. https://ascii.co.uk/art
2. Check the Flowchart 
3. print("") # for single line code block | print('''''') # for multi line code block

Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.

Use the flow chart linked here to create the game logic.

Once you've completed the project, you can always extend the game and make it more interesting!

 Hint 
You can use the lower() function to turn any string into all lower case. https://www.w3schools.com/python/ref_string_lower.asp
Alternatively you can also use the logical operator "or" to check for other spellings of user choice. e.g. Right, right or RIGHT.

https://appbrewery.github.io/python-day3-demo/


'''


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Answer

choice1 = input('Your\re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    # Continue in game
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()

    if choice2 == "wait":
        # game will continue
        choice3 = input('You arrive at the island unharmed. '
                        'There is house with 3 doors. One red, one blue and one yellow. '
                        'Which colour do you choose?\n').lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell in to a hole. Game Over.")

# Answer - My solution
'''
cross_road = input('You\n're at the cross road. Where do you want to go? 
            Type "left" or "right?"')

if cross_road == "left"or cross_road == "Left":
    lake = input('You have come into the the lake.
            Type "swim" or "wait"')
    if lake == "wait" or lake == "Wait":
        door = input('You have come into the final stage choose. Choose the color of your door.
                    Type "red" or "blue" or "yellow"')
        if door == "red" or door == "Red":
            print("Burned by Fire. Game Over")
        elif door == "blue" or door == "Blue":
            print("Eaten by beasts. Game Over")
        elif door == "yellow" or door == "Yellow":
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game over")

'''



