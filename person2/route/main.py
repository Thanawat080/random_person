from flask import Blueprint
from service.predict_img import predict
from function.con_elastic import connect_data
home_bp = Blueprint('home', __name__)


@home_bp.route('/face', methods=['POST'])
def hello():
    for i in range(1000):
        res = predict()
        if res != 'No face detected':
            es = connect_data()
            result = es.index(index='face_generator', body=res, request_timeout=60, doc_type='my_type')
    return 'finish'

@home_bp.route('/image_status/<id>', methods=['PUT'])
def update_imge_status(id):
    es = connect_data()
    doc = {
        "doc": {
            "isUse": True
        }
    }
    results_update = es.update(index="face_generator", id=id, doc_type='my_type', body=doc)
    results_update_search = es.get(index="face_generator", id=id, doc_type='my_type')    
    return results_update_search


