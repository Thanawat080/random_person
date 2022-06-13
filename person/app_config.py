import os

ELASTIC_PASS = os.getenv("ELASTIC_PASS")
if not ELASTIC_PASS:
    ELASTIC_PASS = "rljZekw7TTZG4DjQnv2z"

ELASTIC_USER = os.getenv("ELASTIC_USER")
if not ELASTIC_USER:
    ELASTIC_USER = "elastic"