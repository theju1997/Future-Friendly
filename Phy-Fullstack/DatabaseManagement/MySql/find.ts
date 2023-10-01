var mysql=require('mysql')
var con=mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'',
    database:'Program'
})
con.connect((err:any)=>{
    if(err)throw err;
    console.log('Db connected')

let query="SELECT * FROM `pg_programs` WHERE Coursename"

con.query(query,(err:any,res:any)=>{
    if(err)throw err
    console.log("searched")  
})
})