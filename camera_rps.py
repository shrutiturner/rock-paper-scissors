import random

from run_model import CaptureVideo

class CameraRPS:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_wins = 0
        self.computer_wins = 0

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
                self.computer_wins += 1
                return('Computer wins!')
            self.user_wins +=1
            return('User wins!')
        elif computer_choice == 'paper':
            if user_choice == 'rock':
                self.computer_wins += 1
                return('Computer wins!')
            self.user_wins +=1
            return('User wins!')
        elif computer_choice == 'scissors':
            if user_choice == 'paper':
                self.computer_wins += 1
                return('Computer wins!')
            self.user_wins +=1
            return('User wins!')


    def play(self, wins=3):
        """Runs the camera game of rock, paper, scissors calling functions to get the computer and user choices and determine the winner. Match ends after number of wins is met"""
        
        while True:
            computer_choice = self.get_computer_choice()
            user_choice = self.get_user_choice()
            winner = self.get_winner(computer_choice, user_choice)
            
            print(f"User chose '{user_choice}', Computer chose '{computer_choice}'")
            print(f"{winner} \nUser Score: {self.user_wins} \nComputer Score: {self.computer_wins}")

            if self.computer_wins == wins or self.user_wins == wins:
                break

            while True:
                next = input("Press enter to play next round.")
                if next == '':
                    break
        
        if self.user_wins > self.computer_wins:
            winner = 'User'
        elif self.user_wins < self.computer_wins: 
            winner = 'Computer'
        else:
            print('error')
        
        print(f"Game Over. {winner} wins!")

        return(None)


rps_game = CameraRPS()
rps_game.play()

