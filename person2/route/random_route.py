import sys
sys.path.append("..\person")
from service.random_service import random_person
from function.con_elastic import connect_data
from flask import Blueprint
from function.random_function import  random_function

random_route = Blueprint('random_data', __name__)

@random_route.route("/")
def index():
    user_obj = random_person()
    return user_obj 

# add user
@random_route.route("/", methods=['POST'])
def add_user():  
    es = connect_data()
    user_obj = random_person()
    result = es.index(index="random_user",body=user_obj, doc_type='my_type')
    return user_obj 

@random_route.route("/<id>") 
def index_get(id):
    es = connect_data()
    results = es.get(index="random_user",id=id, doc_type='my_type')
    return dict(results).get('_source')



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

