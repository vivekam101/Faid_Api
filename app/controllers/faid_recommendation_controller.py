import random
from app import config
import pymongo
import pandas as pd
import numpy as np
from odo import odo
import json
from pymongo import MongoClient
from app.ml import recommendation

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


def read_mongo(db="FAID", collection="faid_persona", query={}, host='localhost', port=27017, username=None, password=None):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    return df

def predict(_data):

    _config = config.RECOMMENDATION_API_CONFIG
    _map = _config.get("data_map")

    if _map:
        print("mapping")
        _data = _map(_data)

    print("Data ----->\n")
    print(_data)

    _df = load_object(_data)
    print(_df)
    _df["_id"] = _df["_id"].astype(str)
    _df_mongo = read_mongo(query = {"_id":_df["_id"].values[0]})
    print(_df_mongo)
    # merge based on _id
    _merged_df = pd.merge(_df_mongo, _df, on='_id')
    print(_merged_df)
    recomm_df = recommendation(_merged_df)
    print(recomm_df)

    return recomm_df

