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
let query="UPDATE `pg_programs` SET `Coursename`='[MDes]',`Stream`='[AE]' WHERE Coursename='MDes1'"

con.query(query,(err:any,res:any)=>{
    if(err)throw err
    console.log("Updated")  
})
})