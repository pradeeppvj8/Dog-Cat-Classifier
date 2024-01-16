import numpy as np 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os 

class DogCat:
    def __init__(self, file_name):
        self.file_name = file_name

    def predict_dog_cat(self):
        model = load_model(os.path.join("artifacts","training","model.h5"))
        image_name = self.file_name
        test_image = image.load_img(image_name, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)

        if result[0] == 1:
            prediction = 'Dog'
        else:
            prediction = 'Cat'

        return [{"image": prediction}]
