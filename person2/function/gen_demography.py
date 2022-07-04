from deepface import DeepFace


def predict_image(img):
    
    attributes = ['age', 'gender', 'race']
    demography = DeepFace.analyze(img, attributes)
    return demography
