# Barret Fisher
# barret.fisher@uky.edu
# CS115 Section 5
# 10-23-12
# Program 3
# Purpose: Game of three dice
# Preconditions: User inputs wager amount and number to bet on
# Postconditions: User wins multiple of wager or loses wager based
#                 on random rolls of dice each turn



# BONUS ALERT, this program went turtles up in here



#to roll dice
from random import randint
from turtle import *



# diceTurtles
# Purpose: Draw dice using turtles
# Preconditions: Parameters are 3 dice rolls
# Postconditions: Draws three rolls of dice
def diceTurtles(x,y,z):
    line = Turtle()
    line.ht()
    line.width(2)
    line.speed(0)

    # dice 1
    line.pd()
    line.goto(0,150)
    line.goto(150,150)
    line.goto(150,0)
    line.goto(0,0)
    line.up()
    line.goto(75,75)
    spots(line,x)

    # dice 2
    line.goto(170,0)
    line.pd()
    line.goto(170,150)
    line.goto(320,150)
    line.goto(320,0)
    line.goto(170,0)
    line.up()
    line.goto(245,75)
    spots(line,y)

    # dice 3
    line.goto(340,0)
    line.pd()
    line.goto(340,150)
    line.goto(490,150)
    line.goto(490,0)
    line.goto(340,0)
    line.up()
    line.goto(415,75)
    spots(line,z)



# spots
# Purpose: Draw spots for diceTurtles
# Preconditions: Parameters are turtle and a roll of die
# Postconditions: Draws spots in the dice outlines
def spots(t,x):
    if x == 1:
        t.dot(25)
    elif x == 2:
        t.left(90)
        t.fd(40)
        t.left(90)
        t.fd(40)
        t.left(90)
        t.dot(25)
        t.fd(80)
        t.left(90)
        t.fd(80)
        t.dot(25)
    elif x == 3:
        t.dot(25)
        t.left(90)
        t.fd(40)
        t.left(90)
        t.fd(40)
        t.left(90)
        t.dot(25)
        t.fd(80)
        t.left(90)
        t.fd(80)
        t.dot(25)
    elif x == 4:
        t.left(90)
        t.fd(40)
        t.left(90)
        t.fd(40)
        t.left(90)
        t.dot(25)
        t.fd(80)
        t.dot(25)
        t.left(90)
        t.fd(80)
        t.left(90)
        t.dot(25)
        t.fd(80)
        t.dot(25)
    elif x == 5:
        t.dot(25)
        t.left(90)
        t.fd(40)
        t.left(90)
        t.fd(40)
        t.left(90)
        t.dot(25)
        t.fd(80)
        t.dot(25)
        t.left(90)
        t.fd(80)
        t.left(90)
        t.dot(25)
        t.fd(80)
        t.dot(25)
    else:
        t.left(90)
        t.fd(40)
        t.left(90)
        t.fd(40)
        t.left(90)
        t.dot(25)
        t.fd(40)
        t.dot(25)
        t.fd(40)
        t.dot(25)
        t.left(90)
        t.fd(80)
        t.left(90)
        t.dot(25)
        t.fd(40)
        t.dot(25)
        t.fd(40)
        t.dot(25)


####################### Dice functions are commented out, Turtles are in!
### dice1
### Purpose: Draw side of dice 1
### Preconditions: None
### Postconditions: Prints side of dice 1
##def dice1():
##    print(" _________")
##    print("|         |")
##    print("|         |")
##    print("|    •    |")
##    print("|         |")
##    print("|_________|")
##
### dice2
### Purpose: Draw side of dice 2
### Preconditions: None
### Postconditions: Prints side of dice 2
##def dice2():
##    print(" _________")
##    print("|         |")
##    print("|  •      |")
##    print("|         |")
##    print("|      •  |")
##    print("|_________|")
##
### dice3
### Purpose: Draw side of dice 3
### Preconditions: None
### Postconditions: Prints side of dice 3
##def dice3():
##    print(" _________")
##    print("|         |")
##    print("|  •      |")
##    print("|    •    |")
##    print("|      •  |")
##    print("|_________|")
##
### dice4
### Purpose: Draw side of dice 4
### Preconditions: None
### Postconditions: Prints side of dice 4
##def dice4():
##    print(" _________")
##    print("|         |")
##    print("|  •   •  |")
##    print("|         |")
##    print("|  •   •  |")
##    print("|_________|")
##
### dice5
### Purpose: Draw side of dice 5
### Preconditions: None
### Postconditions: Prints side of dice 5
##def dice5():
##    print(" _________")
##    print("|         |")
##    print("|  •   •  |")
##    print("|    •    |")
##    print("|  •   •  |")
##    print("|_________|")
##
### dice6
### Purpose: Draw side of dice 6
### Preconditions: None
### Postconditions: Prints side of dice 6
##def dice6():
##    print(" _________")
##    print("|         |")
##    print("|  •   •  |")
##    print("|  •   •  |")
##    print("|  •   •  |")
##    print("|_________|")
##
##
##
### draw_dice
### Purpose: To draw one rolled die by using dice functions
### Preconditions: Parameter 1-6 (dice roll)
### Postconditions: Use functions to draw dice side
##def draw_dice(x): #parameters(dice roll)
##    if x > 5:
##        return dice6()
##    elif x > 4:
##        return dice5()
##    elif x > 3:
##        return dice4()
##    elif x > 2:
##        return dice3()
##    elif x > 1:
##        return dice2()
##    else:
##        return dice1()
#########################################################################


# user_num
# Purpose: To get user input
# Preconditions: User inputs number to bet on (1-6)
# Postconditions: Variable with user's number is saved
# 1. define user_num
# 2. prompt user for input 1-6 (number to bet on)
# 3. assign input to variable num
# 4. if num is not 1-6, re-prompt user for correct input
# 5. return value of user num
def user_num():
    print("Please enter a number between 1 and 6 inclusive")
    num = eval(input("Enter the number you want to bet on -->  "))
    num = round(num)
    while num < 1 or num > 6:
        print("Sorry, that is not a good number")
        num = eval(input("Try again.  Enter the number you want to bet on -->  "))
        num = round(num)
    return num



# user_bet
# Purpose: To get user input
# Preconditions: User inputs amount of wager, parameter is current stake
# Postconditions: Returns amount of user's bet
# 1. define user_bet with parameter(stake)
# 2. prompt user for input of amount to wager
# 3. assign input to variable bet
# 4. if bet is not positive, re-prompt user for correct input
# 5. if bet is more than stake, re-prompt user for correct input
# 6. return value of bet
def user_bet(x): #parameters(stake)
    bet = eval(input("What is your bet?   "))
    bet = round(bet,2)
    while bet > x or bet <= 0:
        if bet > x:
            print("  Sorry, you can't bet more than you have")
        elif bet <= 0:
            print("  Sorry, you can't bet 0 or less than zero")
        bet = eval(input("What is your bet?   "))
        bet = round(bet,2)
    return bet



# matches
# Purpose: To determine how many (if any) matches were made after roll
# Preconditions: 4 parameters are user_num and 3 random rolled dice
# Postconditions: Returns number of matches made
# 1. define matches
# 2. use if statement to compare user_num and 3 random rolled dice
# 3. return value based on how many matches (0-3)
def matches(w,x,y,z): #parameters(number, roll_1, roll_2, roll_3)
    match = 0
    if w == x:
        match += 1
    if w == y:
        match += 1
    if w == z:
        match += 1
    return match



# payoff
# Purpose: To determine wins or losses for roll of dice
# Preconditions: 5 parameters are user_num, user_bet, 3 random rolled dice
# Postconditions: Total amount of winnings or amount lost is returned
# 1. define payoff with 5 parameters
# 2. call matches function using parameters to determine number of matches
# 3. use if statement to determine payout amounts
#       4. if 3 match payout is 10 times user_bet
#       5. if 2 match payout is 5 times user_bet
#       6. if 1 match payout is user_bet
#       7. if 0 match payout is negative user_bet
def payoff(v,w,x,y,z): #parameters(number, bet, roll_1, roll_2, roll_3)
    match = matches(v,x,y,z) #arguments(number, roll_1, roll_2, roll_3)
    if match > 2:
        payout = w * 10
        payout = round(payout,2)
        print("You got a TRIPLE match!")
        print("You won $", payout, sep="")
    elif match > 1:
        payout = w * 5
        payout = round(payout,2)
        print("You got a DOUBLE match!")
        print("You won $", payout, sep="")
    elif match > 0:
        payout = w
        print("You got a match!")
        print("You won $", payout, sep="")
    else:
        payout = 0 - w
        print("You lost your bet! $", w, sep="")
    return payout



# 1. define main function
def main():

    # draw turtle screen
    wn = Screen()
    wn.setup(540,200)
    wn.setworldcoordinates(-20,-20,520,180)
    wn.bgcolor("White")
    wn.title("Your dice rolls")
    
    # 2. stake is 1000, play is True
    stake = 1000
    play = True
    
    # 3. greet the user
    print("Play the game of Three Dice!!")
    
    # play must == True to play
    while play:
        
        # set counters
        singles = 0
        doubles = 0
        triples = 0
        misses = 0
        count = 1
        
        # inform user of current stake
        print("You have $", stake, " to bet with.", sep="")
        print()
        
        # 4. while stake is positive run 10 times:
        while stake > 0 and count < 11:
            
            print("Round", count)
            
            # 5. call user_num function
            number = user_num()
            # 6. call user_bet function
            bet = user_bet(stake)
            
            # 7. run RNG for dice rolls
            roll_1 = randint(1,6)
            roll_2 = randint(1,6)
            roll_3 = randint(1,6)
            
##            # 8. call draw_dice function for each roll
##            draw_dice(roll_1)
##            draw_dice(roll_2)
##            draw_dice(roll_3)
            
            # 8. call diceTurtles function for dice roll (BONUS)
            wn.clear()
            diceTurtles(roll_1, roll_2, roll_3)
            
            print("...")
            print("You rolled a", roll_1, "-", roll_2, "-", roll_3, "...")
            
            # 9. check matches
            match = matches(number, roll_1, roll_2, roll_3)
            # 10. keep counter for singles, doubles, triples
            if match > 0:
                if match == 1:
                    singles += 1
                elif match == 2:
                    doubles += 1
                elif match == 3:
                    triples += 1
            else:
                misses += 1
            
            # 11. add payoff to stake and report results of roll
            stake += payoff(number, bet, roll_1, roll_2, roll_3)
            stake = round(stake,2)
            
            # 12. report amount of stake
            print("Your stake is $", stake, sep="")
            print()
            
            # add 1 to count
            count += 1
        
        # 13. Report number of singles, doubles, triples and misses
        print("*****  Singles", singles, "Doubles", doubles, "Triples", triples, "Misses", misses)
        print()
        
        # 14. Ask if the user wants to play some more while stake is still positive
        if stake > 0:
            answer = input("Want to play some more? (y or n) ")
            if answer != "y":
                play = False
                print("But you STILL have money?!! That does not compute!")
            else:
                play = True
                print()
        else:
            play = False
            print("ALL your MONEY is BELONG to ME!")

    # end game message
    print("Thanks for playing!")

    # end turtle screen
    wn.exitonclick()

main()
