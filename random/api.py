from flask import Flask, Response, Request, request
from flask_restful import Api,Resource,abort
from name import generate
import requests
app=Flask(__name__)


@app.route("/")
def index():
    user_obj = generate()
    return user_obj 



if __name__ == "__main__":
    app.run(debug=True)
