from flask import Flask, Response, Request, request
from flask_restful import Api,Resource,abort
from name import generate
import requests
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts='http://elastic:rljZekw7TTZG4DjQnv2z@localhost:9200')
app=Flask(__name__)


@app.route("/")
def index():
    user_obj = generate()
    return user_obj 

@app.route("/", methods=['POST'])
def add_user():
    user_obj = generate()
    result = es.index(index="random_user",document=user_obj)
    return user_obj 

@app.route("/<id>") 
def index_get(id):
    results = es.get(index="random_user",id=id)
    return dict(results).get('_source')


#get all image
@app.route("/all") 
def index_get_all():
    res = es.search(index="random_user", body = {
        'size' : 100,
        'query': {
            'match_all' : {}
        }
    })
    return dict(res)

if __name__ == "__main__":
    app.run(debug=True)