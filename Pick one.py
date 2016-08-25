# TAKE AWAY MESSAGES:
# 1. seperate game logic (model) and game representation (view)
# 2. factor out functionality to functions with descriptive names

import random

# Given a character c and an integer t
# return a string containing c repeated t times
def repeat(c,t):
    s = ""        # initialise the string s with the empty string
    for i in range(0,t):
        s = s + c # append the character c to the end of the string s
    return s


# Given an integer (the number of sticks),
# return a string (representation of the game status)
def showGameStatus(sticks):
    # "STICKS sticks remaining", where STICKS is replaced by the value
    # of the argument sticks
    textual_repr = str(sticks) + " sticks remaining"

    # "||...|", where "|" is repeated STICKS time and STICKS is the
    # value of the argument sticks
    graphical_repr = repeat("|",sticks)

    return graphical_repr

# Given an integer (the number sticks), returns nothing
def showGameStatus_bad(sticks):
    print str(sticks) + " sticks remaining"

# game modes (an integer):
# 0   -> AI
# 1   -> 1vs1
# ... -> undefined (treat it as AI)

# game levels (an integer):
# 0 -> undefined
# 1 -> level 1
# 2 -> level 2
# 3 -> level 3
# n -> undefined

player1 = raw_input("Please select your name player 1: ")

answer = raw_input("Do you want to play alone? (y/n)")
if answer == "y":
    game_mode = 0
    answer = raw_input("What level do you want to play on? (1-3, 3 most difficult)")
    if answer.isdigit():
        # str() takes an integer and returns a string (representation of it)
        # int() takes a string and returns an integer (represented by the string)
        # str("hello") => "hello"
        # int("hej") => crash
        answer_number = int(answer)
        if answer_number >= 1 and answer_number <= 3:
            game_level = answer_number
        else:
            game_level = 1
    else:
        game_level = 1
elif answer == "n":
    game_mode = 1
else:
    game_mode = 1

if game_mode == 1:
    player2 = raw_input("Please select your name player 2")
    print "Welcome", player1, "and", player2
elif game_mode == 0:
    player2 = "AI"
    print "Good luck,", player1

#initialise sticks
sticks = random.randrange(15,25)
print "There are ",sticks," sticks"

turn = False


if game_mode==1:

    while(sticks > 0):
        #byt turn
        turn = not turn
        #player 1's tur
        if turn:
            #turn = True betyder player 1
            print player1,"'s turn"
        else:
            #turn = False betyder player 2
            print player2,"'s turn"
        #make player select stick
        print "select 1 or 2 sticks"
        choice = raw_input()
        if choice == '1':
            sticks = sticks - 1
        elif choice == '2':
            sticks = sticks - 2
        else:
            print "please select a valid option"
            turn = not turn
        print showGameStatus(sticks)

elif game_mode==0:

    while(sticks>0):
        turn = not turn
        #player 1s tur
        if turn:
            print player1,"'s tur"
            print "select 1 or 2 sticks"
            choice = raw_input()
            if choice == '1':
                sticks = sticks - 1
            elif choice == '2':
                sticks = sticks - 2
            else:
                print "Please select a valid option"
                turn = not turn

        else:
            print player2, "'s tur"
            AI_choice = random.randrange(1,3)
            print("AI chose %r" % AI_choice)
            if AI_choice == 1:
                sticks = sticks - 1
            elif AI_choice == 2:
                sticks = sticks - 2

            print showGameStatus(sticks)



#select winner
if turn == True:
    print player1," wins!!!"
else:
    print player2," wins!!!"

