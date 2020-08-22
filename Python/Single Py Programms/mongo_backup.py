from os.path import join
from pymongo import MongoClient
from bson.json_util import dumps
import time
import os

def backup_db(backup_db_dir):
    try:
        client = MongoClient('localhost:27017')
        database = client.semdart_db
        #authenticated = database.authenticate('root','')
        #assert authenticated, "Could not authenticate to database!"
        collections = database.collection_names()
        print(collections)
        for i, collection_name in enumerate(collections):
            col = getattr(database,collections[i])
            collection = col.find()
            jsonpath = collection_name + ".json"
            jsonpath = join(backup_db_dir, jsonpath)
            with open(jsonpath, 'w', encoding="utf8") as jsonfile:
                jsonfile.write(dumps(collection))
    except Exception as e:
        print (e)
time = time.strftime("%m-%d-%Y-%H:%M:%S")
os.chdir('semdart_db_backup')
os.mkdir(time)
os.chdir(time)
print(os.getcwd())
path=os.getcwd()
backup_db(path)
