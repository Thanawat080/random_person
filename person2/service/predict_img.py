import os
import uuid

from function.gen_demography import predict_image
from function.gen_image import generate_image

def predict():
    
    try:
        generate_image()
        file = './dataset/' + str(uuid.uuid4()) + '.png'
        os.rename('./dataset/0.png', file)
        file_path = file
        a = predict_image(file_path)
        res = {
            "age" : a['age'],
            'gender' : a['gender'],
            'race' : a['dominant_race'],
            'path' : file_path,
            'isUse': False
        }
        return res
    except:
        return "No face detected"
