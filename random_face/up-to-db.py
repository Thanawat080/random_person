
from elasticsearch import Elasticsearch
from deepface import DeepFace
from flask import Flask
from elasticsearch import Elasticsearch
import generate_face
import os
import uuid

# random image
def generate_image():
    FaceGenerator = generate_face.FaceGenerator
    test = FaceGenerator(1)
    test.gen_face()

#predict age, gender, race from image
def predict_image(img):
    
    attributes = ['age', 'gender', 'race']
    demography = DeepFace.analyze(img, attributes)
    return demography

#connect elasticsearch
es = Elasticsearch(hosts='https://elastic:DgoBPxddYXE5bWzX_t4d@localhost:9200', verify_certs=False)
app = Flask(__name__)

#Post method for save image and infomation sample: POST:http://127.0.0.1:5000/faceGen
@app.route('/faceGen', methods=['POST'])
def add_face():
    generate_image()
    file = './dataset/' + str(uuid.uuid4()) + '.png'

    os.rename('./dataset/0.png', file)
    file_path = file
    a = predict_image(file_path)
    res = {
        "age" : a['age'],
        'gender' : a['gender'],
        'race' : a['dominant_race'],
        'path' : file_path
    }
    result = es.index(index='face', body=res, request_timeout=60)
    return dict(result)

#get all image
@app.route("/image") 
def index_get():
    res = es.search(index="face", body = {
        'size' : 100,
        'query': {
            'match_all' : {}
        }
    })
    return dict(res)

#run api on port 5000 debug mode == True
if __name__ == '__main__':
    app.run(debug=True, port=5000)
 
