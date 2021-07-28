import pandas
import pymongo
from bson.json_util import dumps, loads
import pandas as pd

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

print("test 6 query sonucundan çıkan veriler dataframe'e")
r = collection.find(query)
l = list(r)
d = dumps(l)
dict_needed = loads(d)
#print(dict_needed)
df = pandas.DataFrame.from_dict(dict_needed)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df.columns)

print("test 7 örnek uygulama")
print("Veritabanını seçin (local)\n")
for db in client.list_databases():
    print(db)
dbinput = input()
selecteddb = client[dbinput]

print("Collection seçin (deneme)\n")

for collection in selecteddb.list_collection_names():
    print(collection)
collectioninput = input()
selectedcollection = selecteddb[collectioninput]

thedataframe = pandas.DataFrame.from_dict(loads(dumps(list(selectedcollection.find()))))
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print("Bütün dataframe:",thedataframe)

print("Yaş ortalamaları:",thedataframe["median_age"])
# print("Query türünü girin (sayı olarak sadece 1 veya 2)")
# print("1. Find\n2. Insert")
# selectedqueryoption = int(input())
#
# if selectedqueryoption == 1:
#     print("Arama querysini detaylı olarak girin. (örn {continent: Asia})")
#     searchquery = dict(input())
#     returnedquery = selectedcollection.find(searchquery)
#     thelist = list(returnedquery)
#     thestring = dumps(thelist)
#     thedict = loads(thestring)
#     thedataframe = pandas.DataFrame.from_dict(thedict)
#     with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#         print(thedataframe)
# elif selectedqueryoption == 2:
#     print()