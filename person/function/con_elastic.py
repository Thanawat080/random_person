from elasticsearch import Elasticsearch

def connect():
    es = Elasticsearch(hosts='https://elastic:DgoBPxddYXE5bWzX_t4d@localhost:9200', verify_certs=False)
    return es

def connect_data():
    es = Elasticsearch(hosts='http://elastic:rljZekw7TTZG4DjQnv2z@localhost:9200')
    return es