


import random
from easygui import *

image_url = "C:/Users/Kumar Kishlay/Desktop/Roulette_game_[2]/Roulette_game_/roulette_im.gif"


bet_size = 100
global exited_number
global number_played
exited_number = ""

numbers = []
for i in list(range(0,37)):
    numbers.append(i)

#Dictionary with even and odd numbers
dictionary_E_O = {}
for i in list(range(0,37)):
    if i == 0:
        dictionary_E_O[i] = "Zero"
    elif i%2 == 0:
        dictionary_E_O[i] = "Even"
    else:
        dictionary_E_O[i] = "Odd"

#Dictionary with red and black numbers
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
dictionary_R_B = {}
for i in list(range(0,37)):
    if i == 0:
        dictionary_R_B[i] = "Na"
    elif i in red:
        dictionary_R_B[i] = "Red"
    else:
        dictionary_R_B[i] = "Black"

#numbers from 1 to 18 and from 19 to 36
one_to_18 = list(range(1,19))
two_to_36 = list(range(19,37))

#Columns
first_column = list(range(1,35,3))
second_column = list(range(2,36,3))
third_column = list(range(3,37,3))

#Rows (12 numbers per row)
first_row = list(range(1,13))
second_row = list(range(13,25))
third_row = list(range(25,37))


def roulette_table_(result):
    if result == 0:
        print("ZERO!!!!!!")
    table = []
    i = 1
    while i <= 34:
        row = [i, i + 1, i + 2]
        table.append(row)
        i += 3
    for i in range(0, 12):
        try:
            index_result = table[i].index(result)
            index_list = i
        except ValueError:
            pass
    table[index_list][index_result] = "X"
    print(table)
    return True


def roulette_spin():
    global exited_number
    result = random.sample(numbers, 1)
    print("Number: " + str(result[0]) + " " + str(dictionary_E_O[result[0]]) + " " + str(dictionary_R_B[result[0]]))
    exited_number = "Number: " + str(result[0]) + " " + str(dictionary_E_O[result[0]]) + " " + str(dictionary_R_B[result[0]])
    roulette_table_(result[0])
    return result[0]

def who_wins_number():
    global number_played
    number = integerbox(msg = 'Odds for numbers: 36 to 1\nEnter the number to bet on:', title='Roulette 1.0', lowerbound = 0, upperbound = 36, image = image_url + "tabe.gif")
    number_played = str(number)
    result = roulette_spin()
    print("Number played: " + str(number))
    if number == result:
        return True
    else:
        return False


def who_wins_even_odd(player_bet):
    result = roulette_spin()
    if player_bet == dictionary_E_O[result]:
        return True
    else:
        return False

def who_wins_red_black(player_bet):
    result = roulette_spin()
    if player_bet == dictionary_R_B[result]:
        return True
    else:
        return False

def who_wins_1to18_19to36(player_bet):
    result = roulette_spin()
    if player_bet == "1 to 18":
        if result in one_to_18:
            return True
        else:
            return False
    elif player_bet == "19 to 36" :
        if result in two_to_36:
            return True
        else:
            return False
    else:
        return False

def who_wins_columns(player_bet):
    result = roulette_spin()
    if player_bet == "first column":
        if result in first_column:
            return True
        else:
            return False
    elif player_bet == "second column":
        if result in second_column:
            return True
        else:
            return False
    elif player_bet == "third column":
        if result in third_column:
            return True
        else:
            return False
    else:
        return False

def who_wins_horizontal(player_bet):
    result = roulette_spin()
    if player_bet == "1 to 12 horizontal":
        if result in first_row:
            return True
        else:
            return False
    elif player_bet == "13 to 24 horizontal":
        if result in second_row:
            return True
        else:
            return False
    elif player_bet == "25 to 36 horizontal":
        if result in third_row:
            return True
        else:
            return False
    else:
        return False

def after_play_win(bet):
    options_win = ["Ok, go on!", "Change bet size"]
    button = buttonbox(msg = "Congrats you won!\n" + "Result: " + exited_number + "\nYour hand: " + str(player_b) + " " + str(number_played), title = "You won!", choices = options_win, image = image_url + "winner.gif" )
    if button == "Change bet size":
        new_bet_size = integerbox(msg = 'Enter new bet size.\nYour available balance: ' + str(player_balance), title='Roulette 1.0', lowerbound = 0, upperbound = player_balance)
        return new_bet_size
    else:
        return bet

def after_play_lost(bet):
    options_lost = ["Ok, go on!", "Change bet size"]
    button = buttonbox(msg = "Sorry, you lost.\n" + "Result: " + exited_number + "\nYour hand: " + str(player_b) +  " " + str(number_played), title = "You lost", choices = options_lost, image = image_url + "dog.gif" )
    if button == "Change bet size":
        new_bet_size = integerbox(msg = 'Enter new bet size.\nYour available balance: ' + str(player_balance), title = 'Roulette 1.0', lowerbound = 0, upperbound = player_balance)
        return new_bet_size
    else:
        return bet    
    


options = ["Red","Black","Even","Odd", "first column", "second column", "third column", "1 to 18", "19 to 36", "1 to 12 horizontal", "13 to 24 horizontal", "25 to 36 horizontal", "Number", "Exit"]
casino_balance = 1000
player_balance = 1000


msgbox(msg = "Roulette 1.0",title = "Roulette 1.0", image = image_url + "roulette_im.gif")

while True:
    #return None if user cancelled selection (cliked on cancel).
    player_b = ""
    number_played = ""
    player_b = buttonbox(msg = "Make your bet!\nHere's your available balance after tha last game: " + str(player_balance), title = "Roulette 1.0", choices = options, image = image_url + "tabe.gif")
    print("Player's bet: " + str(player_b))
    if str(type(player_b)) !=  "<class 'str'>":
        break
    elif player_b == "Exit":
        break
    elif player_b == "Number":
        winner = who_wins_number()
        double_payoff = False
        triple_payoff = False
    elif player_b == "Red" or player_b == "Black":
        winner = who_wins_red_black(player_b)
        double_payoff = True
        triple_payoff = False
    elif player_b == "Even" or player_b == "Odd":
        winner = who_wins_even_odd(player_b)
        double_payoff = True
        triple_payoff = False
    elif player_b == "first column" or player_b == "second column" or player_b == "third column":
        winner = who_wins_columns(player_b)
        triple_payoff = True
        double_payoff = False
    elif player_b == "1 to 18" or player_b == "19 to 36":
        winner = who_wins_1to18_19to36(player_b)
        double_payoff = True
        triple_payoff = False
    elif player_b == "1 to 12 horizontal" or player_b == "13 to 24 horizontal" or player_b == "25 to 36 horizontal":
        winner = who_wins_horizontal(player_b)
        double_payoff = False
        double_payoff = True

    if winner and double_payoff:
        player_balance += 2*bet_size
        casino_balance -= 2*bet_size
        bet_size = after_play_win(bet_size)
    elif winner and triple_payoff:
        player_balance += 3*bet_size
        casino_balance -= 3*bet_size
        bet_size = after_play_win(bet_size)
    elif winner and (not double_payoff) and (not triple_payoff):
        player_balance -= 36*bet_size
        casino_balance += 36*bet_size
        bet_size = after_play_win(bet_size)
    else:
        player_balance -= bet_size
        casino_balance += bet_size
        bet_size = after_play_lost(bet_size)

    print(casino_balance,"casino")
    print(player_balance, "player")

    if player_balance <= 100:
        print("You lost all your available banlance!")
        msgbox(msg = "Sorry, you lost all your available balance!", title = "End of the game", image = image_url + "dog.gif" )
        break






