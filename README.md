# rock-paper-scissors
AiCore Computer Vision project - to create a Rock Paper Scissors game using webcam inputs. The focus of this project is to demonstrate the use of Python flow control.

This README documents the actions taken and decisions made during each step of the project.

Technologies used: Teachable-Machine, Python (keras, numpy, cv2, time, random)

## Milestone 1 - Create the Model
Using Teachable-Machine, an image model with 4 classes (Rock, Paper, Scissors, Nothing) was created using webcam inputs. Default settings were used for number of epochs, learning rate and batch size. The images captured for each class were aimed at being diverse to minimise the risk of overfitting. Three different backgrounds and two different people (with differing gender and race) were used providing both right and left handed gestures. 

The model was downloaded for use in Tensorflow and saved to the repository.

## Milestone 2 - Install the Dependencies
Created a virtual environment to create a reproducable environemnt to manage dependencies. The relevant libraries were installed and a requirements file generated for another user to be able to run the code/to run the code on another device. Provided Python code was run in a script 'run_model.py' to run the keras model downloaded from Teachable-Machine.

## Milestone 3 - Create a Rock-Paper-Scissors Game
A script was created to simulate a manual game of Rock-Paper-Scissors, where the user is asked for a text input for their choice. The computer randomly generates a choice from the options using the 'random' library. The code has been written in functions of single resposibility for clarity and code maintainability. The user input is always converted to lowercase to check its validity, only moving on with the game when a valid input has been accepted using a "while True" loop. The play() function calls the functions created to run the game as a whole.

## Milestone 4 - Use the Camera to Play Rock-Paper-Scissors
The functions to run the manual RPS game were written into a Class, which was then combined in a new script with the output from the run_model.py file which was also rewritten as a Class with associated methods. Logic and console prompts were added to make the game more user friendly, including to repeat the games until the number of wins desired is met (default wins = 3), providing scores and requiring user prompt to go to next round.

## Potential Further Work
The game could be further improved by adding the prompts, including countdown, to the camera display so the entire game can be played without the console. The Computer Vision model has poor accuracy and could be vastly improved by providing more images and variety, and refining the parameters for training. 

## Overall Reflection
This project allowed me to demonstrate my ability to implement logic and write higher quality code, including Classes/Methods and efficient code in terms of reading and running (e.g. minimising repetition) and adhering to PEP8 standards.
