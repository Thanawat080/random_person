from flask import Flask
from route.main import home_bp
from route.random_route import random_route
from flask_cors import CORS
app = Flask(__name__)
import ctypes
from waitress import serve

CORS(app)
app.register_blueprint(home_bp)
app.register_blueprint(random_route)
# app.register_blueprint(contact_bp, url_prefix='/contact')

if __name__ == '__main__':
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    serve(app, host='0.0.0.0', port=8080, threads=1)