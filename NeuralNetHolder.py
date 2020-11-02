#import tensorflow as tf
#from tensorflow import keras
#import numpy as np

class NeuralNetHolder:

    def __init__(self):
        super().__init__()
       # self.trained_model = tf.keras.models.load_model('game_test_model')

    
    def predict(self, input_row):
        # WRITE CODE TO PROCESS INPUT ROW AND PREDICT THRUST, LEFT_TURNING AND RIGHT_TURNING
        float_inputs = [float(x) for x in input_row.split(",")]
        #tf_input = np.array(float_inputs).reshape(1,-1)

        nn_prediction = self.trained_model.predict(tf_input)

        result = [round(x) for x in nn_prediction[0]]
        print(nn_prediction, " --- ", result, " ------ ", float_inputs)
        return result
