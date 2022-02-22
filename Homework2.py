import random
# 0 Rock beats 2 Scissors
# 1 Paper beats 0 Rock
# 2 Scissors beats Paper 1


#function that describes computers choice
def computer_function():
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose Rock")
    elif computer_choice == 1:
        print("Computer chose Paper")
    elif computer_choice == 2:
        print("Computer chose Scissors")
    return computer_choice


#User prompt - enter P, R or S. and User Function
def user_function():
    player_choice = input("Type in R for rock, P for paper, or S for scissors: ").upper()
    if player_choice == "R":
        player_choice = 0
        print("You chose rock")
    elif player_choice == "P":
        player_choice = 1
        print("You chose paper")
    elif player_choice == "S":
        player_choice = 2
        print("You chose scissors")
    else:
        print("Input invalid")
    return int(player_choice)




#Compare function deciding who wins
def compare_function(computer, user):
    if user == 0 and computer == 2:
        print('You Win!')
    elif computer == 0 and user == 2:
        print('Computer Wins!')
    elif computer > user:
        print('You Lose! Computer Won!')
    elif user > computer:
        print('You Won!')
    elif user == computer:
        print('Its a draw!')



user = user_function()

computer = computer_function()

#Comparion of user attempt and computer attempt decising who has won
compare_function(computer,user)