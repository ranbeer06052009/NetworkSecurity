
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://ranbeer6509:tridev06052009@cluster0.4himkwt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


