import random

from run_model import CaptureVideo

class CameraRPS:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']


    def get_computer_choice(self):
        """Generates the computer choice of rock, paper or scissors using random module."""
        
        computer_choice = random.choice(self.choices)

        return computer_choice


    def get_user_choice(self):
        """Asks the user for a camera input of their rock, paper, scissors choice and 
    checks input validity."""

        user_cam = CaptureVideo()

        user_choice = user_cam.get_output()

        return(user_choice)


    def get_winner(self, computer_choice, user_choice):
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


    def play(self):
        """Runs the manual game of rock, paper, scissors calling functions to get the computer and user choices and determine the winner."""
        computer_choice = self.get_computer_choice()
        user_choice = self.get_user_choice()
        winner = self.get_winner(computer_choice, user_choice)
        return(winner)


rps_game = CameraRPS()
print(rps_game.play())

