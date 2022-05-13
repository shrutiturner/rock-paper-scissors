import random

def get_computer_choice():
    """Generates the computer choice of rock, paper or scissors using random module."""
    
    choice_list = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(choice_list)

    return comp_choice

def get_user_choice():
    """Asks the user for a text input of their rock, paper, scissors choice and 
    checks input validity."""

    valid_choices = ['rock', 'paper', 'scissors']

    while True:
        #asks for user input
        user_choice = input("Please enter 'rock', 'paper' or 'scissors': ")

        #checks that the lowercase input matches either rock paper scissors
        if user_choice.lower() in valid_choices:
            return user_choice

        print("Invalid input, please provide one of the specified option ")
    