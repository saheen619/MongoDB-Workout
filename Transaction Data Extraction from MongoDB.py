# Python program to extract all documents from all collections stored in Analytics database and store them to a directory in local system

import pymongo
import bson

from bson import json_util

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace the placeholder with your Atlas connection string
uri = "<Connection String>"

client = MongoClient(uri, server_api=ServerApi('1'))

db=client['sample_analytics']

with open('Transactions Data/accounts.txt', 'w') as f:
    for i in db.accounts.find():
        f.write(json_util.dumps(i) + '\n')
f.close()

with open('Transactions Data/customers.txt', 'w') as f:
    for i in db.customers.find():
        f.write(json_util.dumps(i) + '\n')
f.close()

with open('Transactions Data/transactions.txt', 'w') as f:
    for i in db.transactions.find():
        f.write(json_util.dumps(i) + '\n')
f.close()