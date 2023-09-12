//import {MongoClient} from 'mongodb'
let {Findclint}=require('mongodb')
let mypath="mongodb://127.0.0.1:27017"

let client1=new Findclint(mypath)
let dbName1="Learn-Backend"

async function dbLink(){
  await  client.connect();
  console.log('Connected successfully to server');
  const db = client.db(dbName);
  const collection = db.collection('student');
 let data=await collection.find({}).toArray();
 console.log("checking",data)
}
dbLink()
