import random
from app import config
import pymongo
import pandas as pd
import numpy as np
from odo import odo
import json
from pymongo import MongoClient

def load_object(obj):
    return pd.DataFrame([obj,])

def _connect_mongo(host, port, username, password, db):
    """ A util for making a connection to mongo """

    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db]


def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id:
        del df['_id']

    return df

def insert_to_db(_data):

    _config = config.REGISTRATION_API_CONFIG
    _map = _config.get("data_map")

    if _map:
        print("mapping")
        _data = _map(_data)

    print("Data ----->\n")
    print(_data)

    _df = load_object(_data)

    # derived variable bmi based on height and weight
    _bmi = (_df._weight.astype('float')/(_df._height.astype('float')/100)**2).values
    print(_bmi)
    if _bmi <= 18.5:
        _df["_bmi"] = "under"
    elif _bmi >25:
        _df["_bmi"] = "over"
    else:
        _df["bmi"] = "normal"
    # print(_df._weight/_df._height)
    print(_df['_bmi'])
    connection = MongoClient("localhost", 27017)
    if connection is None:
        # no connection, exit early
        return

    try:
    # get db
        db = connection.FAID
        records = json.loads(_df.T.to_json()).values()
        db.faid_persona.insert(records)
    except:
        print("Connection Problem")
        return False

    return True

