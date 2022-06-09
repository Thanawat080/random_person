from flask import Flask, Response, Request, request
from flask_restful import Api,Resource,abort
from name import generate
import requests
app=Flask(__name__)


@app.route("/")
def index():
    user_obj = generate()
    return user_obj 

@app.route("/face")
def face():
    api = {'api_key':'Wv78mjcR4HC5VWin-YsA2g'}
    x = requests.get('https://api.generated.photos/api/v1/faces',params=api)
    return x.text


if __name__ == "__main__":
    app.run(debug=True)