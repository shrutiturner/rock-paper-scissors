import random


def get_computer_choice():
    """Generates the computer choice of rock, paper or scissors using random module."""
    
    choice_list = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choice_list)

    return computer_choice


def get_user_choice():
    """Asks the user for a text input of their rock, paper, scissors choice and 
    checks input validity."""

    valid_choices = ['rock', 'paper', 'scissors']

    while True:
        #asks for user input
        user_choice = input("Please enter 'rock', 'paper' or 'scissors': ")
        user_choice = user_choice.lower()

        #checks that the lowercase input matches either rock paper scissors
        if user_choice in valid_choices:
            return user_choice

        print("Invalid input, please provide one of the specified option.")


def get_winner(computer_choice, user_choice):
    """Takes two arguments, computer_choice and user_choice, and determined the winner of the rock, paper, scissors game."""
    
    if computer_choice == user_choice:
        return('Draw')
    elif computer_choice == 'rock':
        if user_choice == 'scissors':
            return('Computer wins!')
        return('User wins!')
    elif computer_choice == 'paper':
        if user_choice == 'rock':
            return('Computer wins!')
        return('User wins!')
    elif computer_choice == 'scissors':
        if user_choice == 'paper':
            return('Computer wins!')
        return('User wins!')


def play():
    """Runs the manual game of rock, paper, scissors calling functions to get the computer and user choices and determine the winner."""
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(computer_choice, user_choice)
    return(winner)



print(play())