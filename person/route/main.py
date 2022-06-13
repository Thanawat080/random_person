from flask import Blueprint
from service.predict_img import predict
from function.con_elastic import connect_data
home_bp = Blueprint('home', __name__)


@home_bp.route('/face')
def hello():
    res = predict()
    es = connect_data()
    result = es.index(index='face', body=res, request_timeout=60)
    return dict(result)
    