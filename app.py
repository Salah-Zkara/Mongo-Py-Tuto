import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")

db = conn["ma_base"]["test"]


#insert
D = {"_id":0,"Lname":"ZKARA","Fname":"Salah Eddine","age":19}
L = []
for i in range(1,10):
	D = {"_id":i,"Lname":"ZKARA","Fname":"Salah Eddine","age":20}
	L.append(D)

try:
	db.insert_many(L)
	print("Succes!")
except Exception as e:
	print("ERROR!!")


#find
filter={
    'age': 20
}
limit=3

result = db.find(
  filter=filter,
  limit=limit
)

filtre = {}
resultat = db.find(filtre)
for r in result:
	print(r)


#update
try:
	query = {"age":20}
	newval = {"$set": {"age":54}}
	db.update_many(query,newval)
	print("Ok")
except Exception as e:
	print("ERROR!")


#delete
delete_filter = {"age":54}
db.delete_one(delete_filter)
db.delete_many(delete_filter)


#delete collection
db.drop()