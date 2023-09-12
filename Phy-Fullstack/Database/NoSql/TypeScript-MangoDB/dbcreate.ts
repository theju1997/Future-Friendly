
let {MongoClient1}=require('mongodb')
let myurl="mongodb://127.0.0.1:27017"

let client1=new MongoClient(myaddress)
let db="Learn-Backend"

async function dbLink1(){
  await  client.connect();
  console.log('Connected successfully to server');

  const db = client.db(dbName);
  const collection = db.collection('Student-Details');
 await collection.insertOne({name:'Theju' , qualification:'Msc'})
 console.log("inserted")
}
dbLink1()

