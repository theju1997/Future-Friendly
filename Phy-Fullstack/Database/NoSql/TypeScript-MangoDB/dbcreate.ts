
let {MongoClient}=require('mongodb')
let myaddress="mongodb://127.0.0.1:27017"

let client=new MongoClient(myaddress)
let dbName="Learn-Backend"

async function dbLink1(){
  await  client.connect();
  console.log('Connected successfully to server');

  const db = client.db(dbName);
  const collection = db.collection('Student-Details');
 await collection.insertOne({name:'Theju' , qualification:'Msc'})
 console.log("inserted")
}
dbLink1()
