#from pymongo import MongoClient
#from pymongo.errors import CollectionInvalid
#from collections import OrderedDict
import pandas
import pymongo
from bson.json_util import dumps, loads
import pandas as pd

#client = pymongo.MongoClient("mongodb://localhost:27019/")
client = pymongo.MongoClient('localhost', 27017)

print("test 1 client")
print(client)

print("test 2 database")
db = client["local"]
print(db)

print("test 3 collection")
collection = db["deneme"]
print(collection)

print("test 4 query")
query = { "continent": "Asia" }
print(query)

'''print("test 5")
documents = collection.find(query)
f = open("asia.json", "w")
#for x in documents:
#    f.write(x)
f.write('[')
for document in documents:
    f.write(dumps(document))
    f.write(',')
f.write(']')
f.close()
print("dosyaya yazıldı")'''

print("test 6 query sonucundan çıkan veriler dataframe'e")
r = collection.find(query)
l = list(r) # Converts object to list
d = dumps(l) # Converts to String
dict_needed = loads(d) # Serializes String and creates dictionary
#print(dict_needed)
df = pandas.DataFrame.from_dict(dict_needed)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df.columns)

