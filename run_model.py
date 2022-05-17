import cv2
import numpy as np
import time

from keras.models import load_model


class CaptureVideo:
    def __init__(self) -> None:
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.choices = ['rock', 'paper', 'scissors', 'nothing']

    
    def classify_output(self, prediction):
        """Uses the list of probabilities output from get_output to determine the image in the camera."""
        #get the index of the maximum number in the prediction list
        max_index = np.argmax(prediction)

        #categorise the output based on the index number
        user_category = self.choices[max_index]

        #return category
        return(user_category)


    def countdown(self):
        """Prints console prompt to get ready to play RPS game."""
        print("Make the shape of rock, paper or scissors with your hands in your webcam.")

        for sec in range(3, 0, -1):
            time.sleep(1)
            print(sec)

        return(None)


    def get_output(self):
        """Opens camera and returns the probability that the image belongs to each category (rock, paper, scissors, nothing)."""
        while True: 
            self.countdown()
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            choice = self.classify_output(prediction[0])
            if choice != 'nothing':
                break
            print("Invalid input, please provide one of the specified option.")
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                    
        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        return(choice)

   