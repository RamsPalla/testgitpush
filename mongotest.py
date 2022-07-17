import pymongo
client = pymongo.MongoClient("mongodb+srv://mongodb:Ramsmongodb1@cluster0.xqfssux.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"Rambabu",
    "email":"palla.r7@gmail.com",
    "surname":"Palla"
}

db1 = client["mongotest"]
coll = db1["test"]
coll.insert_one(d)
