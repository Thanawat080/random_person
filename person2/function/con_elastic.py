import sys
sys.path.append("..\person")
from elasticsearch import Elasticsearch
import app_config

def connect_data():
    # password = app_config.ELASTIC_PASS
    # username = app_config.ELASTIC_USER
    es = Elasticsearch(hosts='http://10.10.14.212:9200')
    return es