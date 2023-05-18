
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://satyammarkam123:jacob@cluster0.fh8hexa.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
db = client['sample-db']
collection = db['sample']
car={
    'id': 2,
    'name': 'value2',
    'class':'10nth'
}
result = collection.insert_one(car) 
print(result)

