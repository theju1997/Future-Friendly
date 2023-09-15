
// to run my sql in js first we have to connect db 
var mysql=require('mysql')
var con=mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'',
    // adding db name
    database:'Program'
})
con.connect((err:any)=>{
    if(err)throw err;
    console.log('Db connected')
    // we are changing in let query to create table
let query="CREATE TABLE PG_Programs(Coursename VARCHAR(255),Stream VARCHAR(255))"
con.query(query,(err:any,res:any)=>{
    if(err)throw err
    console.log("Table created")
})
}) 