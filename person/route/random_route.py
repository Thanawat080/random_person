import sys
sys.path.append("..\person")
from service.random_service import random_person
from function.con_elastic import connect_data
from flask import Blueprint

random_route = Blueprint('random_data', __name__)

@random_route.route("/")
def index():
    user_obj = random_person()
    return user_obj 

@random_route.route("/", methods=['POST'])
def add_user():
    es = connect_data()
    user_obj = random_person()
    result = es.index(index="random_user",document=user_obj)
    return user_obj 

@random_route.route("/<id>") 
def index_get(id):
    es = connect_data()
    results = es.get(index="random_user",id=id)
    return dict(results).get('_source')


#get all image
@random_route.route("/all") 
def index_get_all():
    es = connect_data()
    res = es.search(index="random_user", body = {
        'size' : 100,
        'query': {
            'match_all' : {}
        }
    })
    return dict(res)

