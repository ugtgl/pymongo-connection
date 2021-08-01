import pandas
import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client["local"]
collection = db["deneme"]
data = collection.find()
df = pandas.DataFrame.from_dict(collection.find())
df = df[df.duplicated(subset=['continent'])]

a = df.groupby('continent').apply(lambda x: list(x.index))
print (a)

df1 = (df.groupby('continent')
       .apply(lambda x: tuple(x.index))
       .reset_index(name='idx'))
print (df1)


