import pymongo
client = pymongo.MongoClient("mongodb+srv://mongodb:Ramsmongodb1@cluster0.xqfssux.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client["myinfo"]
collection = database["sudh"]

#record = collection.find()
#for i in record:
    #print(i)

#data = collection.find({"companyName":"iNeuron"})
data = collection.find({"courseOffered": {"$gt": "E"}})
for i in data :
    print(i)