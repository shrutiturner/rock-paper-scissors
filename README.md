# rock-paper-scissors
AiCore Computer Vision project - to create a Rock Paper Scissors game using webcam inputs. The focus of this project is to demonstrate the use of Python flow control.

This README documents the actions taken and decisions made during each step of the project.

Technologies used: Teachable-Machine

## Milestone 1 - Create the Model
Using Teachable-Machine, an image model with 4 classes (Rock, Paper, Scissors, Nothing) was created using webcam inputs. Default settings were used for number of epochs, learning rate and batch size. The images captured for each class were aimed at being diverse to minimise the risk of overfitting. 3 different backgrounds and two different people (with differing gender and race) were used providing both right and left handed gestures. 

The model was downloaded for use in Tensorflow and saved to the repository.
