//import {MongoClient} from 'mongodb'

let {MongoClient}=require('mongodb')
let myaddress="mongodb://127.0.0.1:27017"

let client=new MongoClient(myaddress)
let dbName="Learn-Backend"

async function dbLink(){
  await  client.connect();
  console.log('Connected successfully to server');
  const db = client.db(dbName);
  const collection = db.collection('Student-Details');
 let data=await collection.find({qualification:"Msc"}).toArray();
 console.log("check--",data)
}
dbLink()
